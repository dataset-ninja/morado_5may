# Path to the original dataset

import csv
import os

import supervisely as sly
from supervisely.io.fs import get_file_name


def create_ann(image_path, anns_path, ripe_obj_class, raw_obj_class):
    labels = []
    image_np = sly.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]
    file_name = get_file_name(image_path)
    ann_path = os.path.join(anns_path, file_name + ".csv")

    with open(ann_path, "r") as csv_file:
        ann = csv.reader(csv_file)
        for label in ann:
            left = int(float(label[0]))
            top = int(float(label[1]))
            right = int(float(label[2]))
            bottom = int(float(label[3]))
            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            if label[4] == "ripe":
                label = sly.Label(rect, ripe_obj_class)
            else:
                label = sly.Label(rect, raw_obj_class)
            labels.append(label)
    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "../datasets-bot/datasets/morado_5may"
    img_dir = "images"
    ann_dir = "annotations"
    ds_name = "ds0"

    ripe_obj_class = sly.ObjClass("ripe", sly.Rectangle)
    raw_obj_class = sly.ObjClass("raw", sly.Rectangle)
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[ripe_obj_class, raw_obj_class])
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, img_dir)
    anns_path = os.path.join(dataset_path, ann_dir)

    images_names = os.listdir(images_path)

    progress = sly.Progress(f"Create dataset {ds_name}", len(images_names))

    for images_names_batch in sly.batched(images_names):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [
            create_ann(image_path, anns_path, ripe_obj_class, raw_obj_class)
            for image_path in img_pathes_batch
        ]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(images_names_batch))

    return project

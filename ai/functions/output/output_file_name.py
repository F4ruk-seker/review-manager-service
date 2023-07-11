from datetime import datetime


def generate_output_file_name(file_id, extension, header = ''):
    now: datetime = datetime.now()

    formatted_date: str = now.strftime("%d-%m-%Y")
    formatted_time: str = now.strftime("%H-%M")

    file_name: str = f"{header}_{formatted_date}_{formatted_time}_{file_id}.{extension}"
    return file_name


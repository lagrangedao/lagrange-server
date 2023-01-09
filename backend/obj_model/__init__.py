import time

# todo update records
def update_record(record, session):
    current_time = str(int(time.time()))
    updated_at_str = "updated_at"
    if hasattr(record, updated_at_str):
        setattr(record, updated_at_str, current_time)

    updated_on_str = "updated_on"
    if hasattr(record, updated_on_str):
        setattr(record, updated_on_str, current_time)

    update_time_str = "update_time_str"
    if hasattr(record, update_time_str):
        setattr(record, update_time_str, current_time)

    session.add(record)
    session.commit()
    session.flush()
    session.refresh(record)


def add_record(record, session):
    current_time = str(int(time.time()))

    created_at_str = "created_at"
    if hasattr(record, created_at_str):
        setattr(record, created_at_str, current_time)

    created_on_str = "created_on"
    if hasattr(record, created_on_str):
        setattr(record, created_on_str, current_time)

    updated_at_str = "updated_at"
    if hasattr(record, updated_at_str):
        setattr(record, updated_at_str, current_time)

    updated_on_str = "updated_on"
    if hasattr(record, updated_on_str):
        setattr(record, updated_on_str, current_time)
    session.add(record)
    session.flush()
    session.commit()
    session.refresh(record)

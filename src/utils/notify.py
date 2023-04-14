from os import path
from datetime import date, datetime, timedelta
from notifypy import Notify


notification = Notify(
    default_notification_application_name='Налоговый календарь')
notification.title = "Скоро состоится событие"


def send_notify(message: str, icon_path: str) -> None:
    notification.icon = icon_path
    notification.message = message
    notification.send()


def send_reminder_notifications(reminders, settings, icon_path: str):
    for reminder in reminders.get_all():
        reminder_date = datetime.strptime(reminder['date'], '%a %b %d %Y')
        current_date = datetime(
            year=date.today().year,
            month=date.today().month,
            day=date.today().day
        )
        diff = current_date - reminder_date
        delay = settings.get_by_key('delay_value', 0)

        # FIXME: timedelta вынести в настройки приложения
        if diff <= timedelta(hours=delay) and diff >= timedelta(hours=-delay):
            send_notify(reminder['title'], icon_path)

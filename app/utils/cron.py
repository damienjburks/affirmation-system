"""
DefaultScheduler Module
This module provides a DefaultScheduler class that uses APScheduler to run jobs at specified intervals.
"""

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from routers.affirmation_v1 import send_affirmation_message


class DefaultScheduler:
    """
    A class to schedule and run the various jobs periodically.
    """

    def __init__(self, interval_hours=24):
        """
        Initializes the CronJob Class.

        Args:
            interval_hours (int): The interval in hours at which the DefaultScheduler should run.
        """
        self.scheduler = BackgroundScheduler()
        self.interval_hours = interval_hours

    def start(self):
        """
        Starts the scheduler and schedules jobs.
        """
        logging.info("Starting scheduler...")
        self.scheduler.add_job(
            self._run_affirmation_job,
            trigger=CronTrigger(hour=7, minute=0, timezone="America/Chicago"),
            id="affirmation_job",
            name="Run affirmation job every day at 7:00 AM CST",
            replace_existing=True,
        )
        self.scheduler.start()
        logging.info("Scheduler started.")
        logging.info("Scheduler will run every %d hours.", self.interval_hours)

    def _run_affirmation_job(self):
        """
        Runs the affirmation job.
        This method should contain the logic to generate and send affirmations.
        """
        logging.info("Running affirmation job...")
        message = send_affirmation_message()
        if message:
            logging.info("Affirmation sent successfully: %s", message)
        else:
            logging.error("Failed to send affirmation.")
        logging.info("Affirmation job completed.")

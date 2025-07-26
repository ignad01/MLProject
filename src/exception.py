import sys
from src import logger


def error_message_details(error, error_details: sys):
    """
    Returns a string containing the details of the last exception raised.
    """
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error massage [{2}]".format(
        file_name, exc_traceback.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_massage, error_detail: sys):
        super().__init__(error_massage)
        self.error_message = error_message_details(error_massage, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logger.logging.info("Divide by Zero")
        raise CustomException(e, sys)

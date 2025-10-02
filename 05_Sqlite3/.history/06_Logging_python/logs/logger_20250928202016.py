import logging

# Remove old handlers if any
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Create handlers for both file and console
file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()

# Set logging level
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)

# Set format for both handlers
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

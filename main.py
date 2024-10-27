
from ImageOrganizer import ImageOrganizer


org = ImageOrganizer('C:\\GIT\\Image-Organizer\\test')
org.rename_files_with_datetime()
org = ImageOrganizer('C:\\GIT\\Image-Organizer\\test')
org.sort_by_year('my_images')



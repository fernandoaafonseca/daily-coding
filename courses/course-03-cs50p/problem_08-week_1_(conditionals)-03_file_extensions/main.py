'''
File Extensions

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
'''


def main():
    user_file_name = input('File name: ')
    user_file_media_type, user_file_media_extension = check_user_file(
        user_file_name)
    print(final_text_media_type_and_extension(
        user_file_media_type, user_file_media_extension))


def check_user_file(file_name):
    file_name = file_name.strip().lower()
    file_media = file_name.split('.')

    try:
        file_media_extension = file_media[-1]
    except:
        file_media_type = 'application'
        file_media_extension = 'octet-stream'
        return file_media_type, file_media_extension

    match file_media_extension:
        case 'gif':
            file_media_type = 'image'
        case 'jpg':
            file_media_type = 'image'
            file_media_extension = 'jpeg'
        case 'jpeg':
            file_media_type = 'image'
        case 'png':
            file_media_type = 'image'
        case 'pdf':
            file_media_type = 'application'
        case 'txt':
            file_media_type = 'text'
            file_media_extension = 'plain'
        case 'zip':
            file_media_type = 'application'
        case _:
            file_media_type = 'application'
            file_media_extension = 'octet-stream'

    return file_media_type, file_media_extension


def final_text_media_type_and_extension(media_type, media_extension):
    return f'{media_type}/{media_extension}'


main()


# Test:
media_type, media_extension = check_user_file('happy.jpg')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'image/jpeg')

media_type, media_extension = check_user_file('document.pdf')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'application/pdf')

media_type, media_extension = check_user_file('cat.gif')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'image/gif')

media_type, media_extension = check_user_file('document.txt')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'text/plain')

media_type, media_extension = check_user_file('cat')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'application/octet-stream')

media_type, media_extension = check_user_file('extra_extension_test.txt.pdf')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'application/pdf')

media_type, media_extension = check_user_file('uppercase_test.PDF')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'application/pdf')

media_type, media_extension = check_user_file('   blank_spaces_test.zip')
print(final_text_media_type_and_extension(
    media_type, media_extension) == 'application/zip')

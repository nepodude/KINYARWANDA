#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

void playsound(const char *filepath){
    char command[1050];
    snprintf(command, sizeof(command), "aplay %s", filepath);
    int ret = system(command);
    if (ret != 0)
    {
        perror("Error playing sound");
    }
}

int main()
{
    const char *dir_path = "./sounds";
    struct dirent *entry;
    DIR *dir = opendir(dir_path);

    if (dir == NULL)
    {
        perror("Unable to open directory");
        return EXIT_FAILURE;
    }

    printf("playing all sounds in file:'%s'", dir_path);

    while((entry = readdir(dir)) != NULL)
    {
        if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0)
        {
            char filepath[1024];
            snprintf(filepath, sizeof(filepath), "%s%s", dir_path, entry->d_name);
            playsound(filepath);
        }
    }
    closedir(dir);

    printf("Played all sound files");
    return EXIT_SUCCESS;
}
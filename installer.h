/**
 * @file installer.h
 * @author Aniket Kumar
 * @brief This the installer of Csq 
 * @version 0.1
 * @date 2023-01-19
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include <stdlib.h>
#include <stdio.h>
//Function to clone the Csq4 respo from github.
void installCsq(){
    system("git clone https://github.com/CsqLang/Csq4.git");
    printf("Installed Csq4 (Done)\n");
}
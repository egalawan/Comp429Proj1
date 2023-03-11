# Chat Application
    
## Team
>Noel Ortiz 
and
>Don Thisura Nawalage
   
    Comp 429 Computer Software Security
    ONLINE CLASS - Friday 7:00 PM - 9:45 PM

## Contributions 
    Noel Ortiz, the Lead Programmer
        - Started reasearching Socket Programming and watched lots of 
        - worked on the set up of the code
        - Worked on most of the methods including the connect(), list_opt(), terminate_opt(), and send_opt()
        - Made the functions work for terminate_opt()
    
    Don Thisura Nawalage, Programmer
        - Worked on bugs that would come up throughout the project
        - Set up the github so that both of us can access the code easily and update eachother
        - Worked on the menu of the application for when the user opens the Application
        - Got the list_opt properly printing out the right IP Address because everytime we tried retrieving the remote port number, we kept getting the <OSError> Socket Not Connected Error and to fix it we added a try and except function
        - Work on the help_opt() and set it up so that the user can understand how to properly use our application if they get stuck
    
## Application Requirements
    - Computer with a command line and something to install python3
        Mac Terminal
            - Follow one of the ways to Download "Homebrew" on mac from https://docs.brew.sh/Installation
            - Once Homebrew is installed, use the following command to install Python 3:
> brew install python
            
            - Then to see if python3 was properly downloaded onto your device and to check the version number do the following command:
> python3 --version
            
        Windows Terminal  
            - Go to the official Python website at https://www.python.org/downloads/ and follow one of the ways to download python3
            - Then to see if python3 was properly downloaded onto your device and to check the version number do the following command:
> python3 --version

            -If python3 was not downloaded try to restart computer
    
## Run Program
    To run the program on Computer:
    - Open Terminal and find the 'project.py' file using cd to go through the folder
> cd 'Path to file'
    
    - Use to ls to see if you can see the file 
> ls

    - If 'project.py' shows up that means youre in the right directory
    - After locating the file use the python3 command to prompt the file and put your port number('1000-6000')
> python3 project.py 3030
    
    - Then the application has started up and the Menu will pop up onto the command line on the terminal. 
    - Then type 'help' to see the functionalities of the application and how to run


   

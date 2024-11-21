A lot of this video to transcript converter was made using the help of previous Assembly AI github repositories
much of which was modified and tweaked in order to mesh together with ffmpeg to get one script to 
convert the whole video (if only in steps)

In order for this to work there are a couple prerequisites
 
- Make your own Assembly AI account and use your personal key! Assembly AI allowes up to 50$ of credits per
free account, and I'm unsure if it renews or not. The Assembly_Key file has a placeholder fake key that 
you need to modify and change out with your own key. Simple copy and paste :)

- Make sure ffmpeg is installed on your computer. To make this is a bit simpler, I think it is just using whatever 
package installer you have in your virtual environment to get ffmpeg up and running. I made this on windows
however which means there are a couple different ways to do this. Personally I installed it manually through
the website and included it in the "Path" for the computer. In your virtual environment, the "subprocess"
takes care of any future use for ffmpeg. 

- Double check which packages are installed in the environment your are running the script in. This can be
especially sneaky with the "requests" import!

As far as usage, run the voice_to_transcript script (in either your virtual environment or the consoleand it will 
prompt for the name of a video file. If giving it the name doesn't work, refer to the below tip. 

Also, if your video is in the same folder as the scripts, you only need to give the name, if it is not, you must
give the absolute path (relative vs absolute path)

That should be all the set up needed in order for the script to work, if there are any more that I forgot I'll 
update this README and upload it back to this github, probably keep a changelog at the bottom too. 

P.S. some of the importing is not optimized i.e. there are double imports, it should still work if all of the 
requirements are satisfied above. 




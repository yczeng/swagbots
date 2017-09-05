# swagBots
Late May 2017, I figured out that theSkimm's referral system doesn't actually check that subscribed emails are real, so I wrote a bot to get free swag by scraping a list of the most common baby names, appending @gmail.com to create subscriber email addresses, and simulating mouse clicks & keyboard strokes. I also tried this for Finimize and theHustle, but only received swag from theskimm.

This is pretty unethical and I mostly did this to see if these sites would would recognize that (such an obvious) bot was doing this. Feel free to browse code but for fucks sake, don't try it on theskimm because they will actually send you swag.

# How to Use:
I used [PyUserInput](https://github.com/SavinaRoja/PyUserInput) by SavinRoja, licensed by GPL-3.0, to simulate mouse clicks and keyboard strokes.

```
sudo pip install PyUserInput
```
You may need to adjust line 26, depending on the size of your monitor.

Run the scripts:
```
python theskimmbot.py
python thehustle.py
python finimizebot.py
```

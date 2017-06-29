# swagBots
Late May 2017, I figured out that theSkimm's referral system doesn't actually check that subscribed emails are real, so I wrote a bot to increase my referral count and get free swag.

After I maxed out the prize pool for theSkimm's referral system, I wrote bots for similar newsletters Finimize and theHustle.

# How does this work?
I scraped a list of the most common baby names and appended @gmail.com to create subscriber email addresses.

Then I simulated mouse clicks and keyboard strokes to navigate the browser.

Leave swagBots running for a couple hours and see your referral count increase!

# How to Use:
I used [PyUserInput](https://github.com/SavinaRoja/PyUserInput) by SavinRoja, licensed by GPL-3.0, to simulate mouse clicks and keyboard strokes.

```
git clone https://github.com/SavinaRoja/PyUserInput
cd PyUserInput
sudo pip3 install PyUserInput
```
For theSkimm, you may need to adjust line 26, depending how the size of your monitor.

Now all you have to do is run the python programs.
```
python theskimmbot.py
python thehustle.py
python finimizebot.py
```

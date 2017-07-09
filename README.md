# swagBots
Late May 2017, I figured out that theSkimm's referral system doesn't actually check that subscribed emails are real, so I wrote a bot to increase my referral count and get free swag.

I scraped a list of the most common baby names and appended @gmail.com to create subscriber email addresses. Then I simulated mouse clicks and keyboard strokes to navigate the browser.

After I maxed out the prize pool for theSkimm's referral system, I wrote bots for similar newsletters Finimize and theHustle.

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

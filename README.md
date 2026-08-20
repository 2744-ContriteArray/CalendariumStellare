# About
The production teams for Star Trek have always been rather inconsistent with how stardates work, and at times intentionally so! Let's fix this and create a universal calendar based on the stars!

# Units
The most basic units in the stardate system are based on the pulsar **J1850-0026** which has a pulse period of 0.1666 seconds [(Source)](https://academic.oup.com/mnras/article/395/2/837/1747062?login=false#25763396).

| Unit        | Definition                                                        |
| ----------- | ----------------------------------------------------------------- |
| **Seconds** | The amount of time it takes for<br>J1850-0026 to rotate 6 times   |
| **Minutes** | The amount of time it takes for<br>J1850-0026 to rotate 360 times |
| **Hours**   | 60 minutes                                                        |
| **Days**    | 30 hours                                                          |
| **Years**   | 360 days                                                          |


# Conversion from Earthly Calendars
Our primary method for calculating Stardates is by converting from the Julian calendar (**not** the Julian *day*) because it's far more regular than the Gregorian calendar currently in common use. So we have two conversion operations we need to do. First from Gregorian to Julian, and then from Julian to Stardate!

### Gregorian conversion to Julian Calendar
The Julian calendar is fairly simple to convert to from the Gregorian calendar since it's ahead by approximately 13 days. So we use the following formula:
				$JC = GC-D$
Where $D$ is the gap of 13 days. This is typically listed as the conversion for dates between 1901 CE and 2099 CE. $D$ increases by 3 days every 400 years (about 0.0075 days per year) so we then need to account for this in our function.

### Converting Julian Calendar to Stardate
Our formula then for converting to a stellar year ($SY$) is 
		$SY = floor(\frac{H/30 - Y*0.25}{360})$
where $Y$ is the Julian years since (*zero day tbd*), $D$ is the Julian *days* since (*zero day tbd*), and $H$ is the *hours* since then. We start by taking $H$ and dividing by 30 to get the stellar days since (*zero day tbd*). Then we multiply $Y$ by $\frac{1}{4}$ and then subtract the product to negate leap years. This calendar isn't based on Earth so we don't need to account for those! We then divide all of that by 360 to get the year, and we round it down with the $floor()$ function to remove floating point digits created from the incomplete day and year.

# Calculation Independent of Earth Calendars

Stardates are counted onward from (*zero day tbd*).

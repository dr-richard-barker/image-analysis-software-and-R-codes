# Spectrum sticker

<figure><img src=".gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>



**spectra in .csv** files for each of the colored squares on the Astrobotany sticker.&#x20;

**Experimental design:** There are six single-point spectra for each color (red, blue, yellow, green, black), collected from six separate Astrobotany stickers. These spectra have been radiance- and reflectance-corrected so that (theoretically) the spectra are agnostic to the illumination source, with a value of 1 in each waveband corresponding to the average value of the standardizing reflectance panel (Spectralon).

**Assay hardware:** Images were taken with Headwall Nano-Hyperspec (400-1000 nm, 269 wavebands). Some of the wavebands in the shorter part of the spectrum are a bit noisy as an artifact of the sensor, but overall I think the shape of the spectra are fine.

## **Julius analysis**

**Prompt:** spectra in .csv files for each of the colored squares on the Astrobotany sticker. There are six single-point spectra for each color (red, blue, yellow, green, black), collected from six separate Astrobotany stickers. These spectra have been radiance- and reflectance-corrected so that (theoretically) the spectra are agnostic to the illumination source, with a value of 1 in each waveband corresponding to the average value of the standardizing reflectance panel (Spectralon). Images were taken with Headwall Nano-Hyperspec (400-1000 nm, 269 wavebands). Some of the wavebands in the shorter part of the spectrum are a bit noisy as an artifact of the sensor, but overall I think the shape of the spectra are fine. Perform exploratory analysis and produce some graphs to summarize the data.

**Response:** I will load the data from the blue.xlsx file and then perform exploratory analysis on the data. I will then generate some graphs to summarize the data.

`The code ran successfully and loaded the data from the blue.xlsx file. The data is in a pandas DataFrame with 7 columns: wavelength, (399, 938), (549, 921), (545, 1087), (392, 1093), (252, 1103), and (90, 1110). The first column is the wavelength in nanometers, and the remaining columns are the reflectance values for each waveband.`

## dataframe: **blue.csv**

import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Plot the spectra for each color

`for k, v in dataframes.items(): print('dataframe: '+ k) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], v['(399, 938)'], label='(399, 938)') plt.plot(v['wavelength'], v['(549, 921)'], label='(549, 921)') plt.plot(v['wavelength'], v['(545, 1087)'], label='(545, 1087)') plt.plot(v['wavelength'], v['(392, 1093)'], label='(392, 1093)') plt.plot(v['wavelength'], v['(252, 1103)'], label='(252, 1103)') plt.plot(v['wavelength'], v['(90, 1110)'], label='(90, 1110)') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Spectra for ' + k) plt.legend() plt.show() print('done')`



<figure><img src=".gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>



### I will now perform some additional analysis on the data to get a better understanding of the differences between the spectra for each color.



import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Calculate the mean reflectance for each color

`for k, v in dataframes.items(): print('dataframe: '+ k) mean_reflectance = v.iloc[:, 1:].mean(axis=1) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], mean_reflectance, label='Mean Reflectance') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Mean Reflectance for ' + k) plt.legend() plt.show() print('done')`



<figure><img src=".gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>



import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Calculate the standard deviation of the reflectance values for each color

`for k, v in dataframes.items(): print('dataframe: '+ k) std_reflectance = v.iloc[:, 1:].std(axis=1) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], std_reflectance, label='Standard Deviation') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Standard Deviation of Reflectance for ' + k) plt.legend() plt.show() print('done')`





<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Calculate the correlation between the reflectance values for each waveband

`for k, v in dataframes.items(): print('dataframe: '+ k) correlation_matrix = v.iloc[:, 1:].corr() plt.figure(figsize=(10, 6)) plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest') plt.colorbar() tick_marks = np.arange(len(v.columns[1:])) plt.xticks(tick_marks, v.columns[1:], rotation=45) plt.yticks(tick_marks, v.columns[1:]) plt.title('Correlation Matrix for ' + k) plt.show() print('done')`

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>









## Now Green



<figure><img src=".gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

`import pandas as pd import matplotlib.pyplot as plt from tqdm import tqdm tqdm.pandas() FILEPATH = './green_(1)_.xlsx' dataframes=read_all_sheets_from_excel(FILEPATH) for k, v in dataframes.items(): print('dataframe: '+ k) print(v.head(15)) print('done')`







import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Plot the spectra for each color

`import pandas as pd import matplotlib.pyplot as plt from tqdm import tqdm tqdm.pandas() FILEPATH = './green_(1)_.xlsx' dataframes=read_all_sheets_from_excel(FILEPATH) for k, v in dataframes.items(): print('dataframe: '+ k) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], v['(397, 961)'], label='(397, 961)') plt.plot(v['wavelength'], v['(548, 947)'], label='(548, 947)') plt.plot(v['wavelength'], v['(546, 1108)'], label='(546,1108)') plt.plot(v['wavelength'], v['(394, 1115)'], label='(394, 1115)') plt.plot(v['wavelength'], v['(253, 1121)'], label='(253, 1121)') plt.plot(v['wavelength'], v['(92, 1131)'], label='(92, 1131)') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Spectra for ' + k) plt.legend() plt.show() print('done')`

<figure><img src=".gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>



import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Calculate the mean reflectance for each color

`import pandas as pd import matplotlib.pyplot as plt from tqdm import tqdm tqdm.pandas() FILEPATH = './green_(1)_.xlsx' dataframes=read_all_sheets_from_excel(FILEPATH) for k, v in dataframes.items(): print('dataframe: '+ k) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], v['(397, 961)'], label='(397, 961)') plt.plot(v['wavelength'], v['(548, 947)'], label='(548, 947)') plt.plot(v['wavelength'], v['(546, 1108)'], label='(546,1108)') plt.plot(v['wavelength'], v['(394, 1115)'], label='(394, 1115)') plt.plot(v['wavelength'], v['(253, 1121)'], label='(253, 1121)') plt.plot(v['wavelength'], v['(92, 1131)'], label='(92, 1131)') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Spectra for ' + k) plt.legend() plt.show() print('done')`

<figure><img src=".gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>



import pandas as pd import matplotlib.pyplot as plt import numpy as np

FILEPATH = './blue.xlsx' dataframes=read\_all\_sheets\_from\_excel(FILEPATH)

### Calculate the standard deviation of the reflectance values for each color

`for k, v in dataframes.items(): print('dataframe: '+ k) std_reflectance = v.iloc[:, 1:].std(axis=1) plt.figure(figsize=(10, 6)) plt.plot(v['wavelength'], std_reflectance, label='Standard Deviation') plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.title('Standard Deviation of Reflectance for ' + k) plt.legend() plt.show() print('done')`



### Calculate red

`import pandas as pd import matplotlib.pyplot as plt from tqdm import tqdm tqdm.pandas() FILEPATH = './red.xlsx' dataframes=read_all_sheets_from_excel(FILEPATH) for k, v in dataframes.items(): print('dataframe: '+ k) print(v.head(15)) print(v.describe()) plt.figure() plt.plot(v['wavelength'], v['(397, 983)']) plt.title('Spectrum for ' + k) plt.xlabel('Wavelength (nm)') plt.ylabel('Reflectance') plt.show() print('done')`

<figure><img src=".gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>






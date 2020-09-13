## COVID COMMAND LINE TOOL

### 1. WHY

So may of these covid tools exist online and I made this one for the sake of learning an also because browsing the web for data is a pain. (Why waste 10 minutes browsing for data when you can spend 15 hours automating the process 😅)

### 2. WHAT

This tool fetches data about the COVID-19

### 3. USAGE

#### Screenshots

![Sample 1](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot1.PNG)

![Sample 2](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot2.PNG)

![Sample 3](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot3.PNG)

#### Commands

```bash
Usage: covtool [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  get           Get Covid Data
  info          Information About The Tool
  plot-country  Plot Country's Time Series Plot by catergory i.e...
  plot-global   Plot Global Time Series Plot by catergory i.e...
  update        Updates Cached Dataset

```

#### 1. get

Shows the different cartegories of covid related data

**_Example_**

```bash
 covtool get --world
```

```bash
TotalCases: 29,029,976
NewCases: +98,561
TotalDeaths: 925,690
NewDeaths: +1,610
TotalRecovered: 20,892,634
NewRecovered: +92,445
ActiveCases: 7,211,652
Serious,Critical: 60,898
TotalCases/1M pop: 3,724
Deaths/1M pop: 118.8
```

**_Example_**

```bash
 covtool get --country Russia
```

```bash
TotalCases: 1,062,811
NewCases: +5,449
TotalDeaths: 18,578
NewDeaths: +94
TotalRecovered: 876,225
NewRecovered: +2,690
ActiveCases: 168,008
Serious,Critical: 2,300
TotalCases/1M pop: 7,282
Deaths/1M pop: 127

```

> **Options**:

> -w, --world Get World-Wide Covid Numbers

> -j, --json Print the Data in Json Format

> -c, --country TEXT Get a Country's Covid Numbers

#### 2. plot-global

```bash
Usage: covtool plot-global [OPTIONS]
                              [[recovered|confirmed|deaths]]

  Plot Global Time Series Plot by catergory i.e recovered|confirmed|deaths
  e.g covtool plot-global confirmed

Options:
  --help  Show this message and exit.
```

**_Example_**

```bash
 covtool plot-global recovered
```

![Global recovered cases](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot4.PNG)

#### 3. plot-country

```bash
Usage: covtool plot-country [OPTIONS]
                               [[recovered|confirmed|deaths]]

  Plot Country's Time Series Plot by catergory i.e
  recovered|confirmed|deaths e.g covtool.py plot-county -n US recovered

Options:
  -n, --name TEXT  Name of the Country  [required]
  --help           Show this message and exit.

```

**_Example_**

```bash
  covtool plot-country --name Kenya confirmed
```

![Country Specific Cases](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot5.PNG)

#### 4. update

```bash
Usage: covtool.py update
```

Updates locally cached dataset

#### 5. Info

```bash
Usage: covtool info [OPTIONS]

  Information About The Tool

Options:
  --help  Show this message and exit.

```

Updates locally cached dataset

![Country Specific Cases](https://github.com/amayomode/Covid-Command-Line-Tool/blob/master/screenshots/screenshot6.PNG)

#### 4. INSTALLATION

To try it out run:

```bash
pip install https://github.com/amayomode/Covid-Command-Line-Tool/raw/master/dist/covtool-0.1.0-py3-none-any.whl
```

Then you can run any command as follows

```bash
 covtool <insert command here>
```

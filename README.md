diet
====

Scripts, reference table of food composition and diet that I used during drying.

### Why

Diet while drying requires careful adjustment. One of the keys to succssful
fat drop is to spend more energy than receive, and also to balance fat/prot/carb
proportion. I used this collection to help me reach that goal.

### What

This repo contains:

* reference.csv - reference table of food composition collected by me from
  actual food boxes. Reference table includes: name, fat, proteins,
  carbohydrates, calories and cost (all values are per 100g of the product).

* day.csv - sample list of products and their mass that I consume during a day.

* conky-calories.conf - sample conky script that I use to display today's
  food comsumption.

* conky-food.conf - sample food.

* calories.py - script that calculates how much of food components you have
  in your daily diet.

### Example

Reference table of food consumption:

```
$ column -s, -t < reference.csv
name                         fat   prot  carb  cal    cost
овсянка                      6.2   12.3  61.8  352    0
рис                          1     6.5   79    350    0
индейка                      7     19    0     140    0
кукуруза                     1.3   3     20.5  112    0
булочка                      2.8   8.7   51.4  265    0
булочка_боско                1     9     52    253    0
творог_вкуснотеево           0.5   18    3.3   89.7   0
творог_дмитровский           1.8   18    3.3   101    30
творог_ростаргоэкспорт       1.8   18    3.3   101    0
молоко_15                    1.5   3     4.7   44     6.2
огурцы_короткоплодные_дикси  0.1   0.8   3     15     0
томаты_дикси                 0.2   0.6   4.2   19     0
болгарский_перец_красный     0.1   1.3   4.9   26     0
яйца                         11.5  12.7  0.7   157    0
кефир_1                      1     3     4     156    0
тунец                        0.4   20.2  0     88.2   51.3
хлеб                         6.8   9.8   44.3  281    0
курага                       0.3   5.2   51    232    0
чернослив                    0.4   2     64    240    0
горох                        0.7   5.5   7.4   73     0
сыр_российский               27    22.5  0     333    0
миндаль                      56    22    12    640    0
кешью                        55.3  26    13    650.7  0
```

Sample diet output for 2 days:

```
$ python calories.py reference.csv 2day.csv 3day.csv
reference.csv 2day.csv
                             mass   fat   prot  carb     cal  cost
болгарский_перец_красный      105   0.1    1.4   5.1    27.3     0
булочка_боско                  30   0.3    2.7  15.6    75.9     0
индейка                       405  28.4   77.0   0.0   567.0     0
огурцы_короткоплодные_дикси   215   0.2    1.7   6.5    32.2     0
рис                            60   0.6    3.9  47.4   210.0     0
творог_ростаргоэкспорт        360   6.5   64.8  11.9   363.6     0
томаты_дикси                  170   0.3    1.0   7.1    32.3     0
яйца                          205  23.6   26.0   1.4   321.9     0
total                        1550  60.0  178.5  95.0  1630.2     0
total_%                         0  18.0   53.5  28.5     0.0     0
reference.csv 3day.csv
                               mass   fat   prot   carb     cal   cost
булочка_боско                  30.0   0.3    2.7   15.6    75.9    0.0
индейка                       200.0  14.0   38.0    0.0   280.0    0.0
кефир_1                       200.0   2.0    6.0    8.0   312.0    0.0
кукуруза                      135.0   1.8    4.0   27.7   151.2    0.0
курага                         20.0   0.1    1.0   10.2    46.4    0.0
овсянка                        33.0   2.0    4.1   20.4   116.2    0.0
огурцы_короткоплодные_дикси   115.0   0.1    0.9    3.5    17.2    0.0
рис                            60.6   0.6    3.9   47.9   212.1    0.0
творог_дмитровский            180.0   3.2   32.4    5.9   181.8   54.0
томаты_дикси                   80.0   0.2    0.5    3.4    15.2    0.0
тунец                         185.0   0.7   37.4    0.0   163.2   94.9
хлеб                           50.0   3.4    4.9   22.1   140.5    0.0
чернослив                      20.0   0.1    0.4   12.8    48.0    0.0
total                        1308.6  28.5  136.3  177.4  1759.7  148.9
total_%                         0.0   8.3   39.8   51.9     0.0    0.0
```

### Author

(c) 2015 Yuri Bochkarev

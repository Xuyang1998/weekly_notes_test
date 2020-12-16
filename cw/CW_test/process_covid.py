# FIXME add needed imports
import matplotlib.pyplot as plt
import json
import math
from jsonschema import validate


def load_covid_data(filepath):
    standard_schema = {
        "type": "object",
        "properties": {
            "metadata": {
                "required": [
                    "time-range",
                    "age_binning"
                ],
                "properties": {
                    "time-range": {
                        "required": [
                            "start_date",
                            "stop_date"
                        ],
                        "properties": {
                            "start_date": {
                                "type": "string"
                            },
                            "stop_date": {
                                "type": "string"
                            }
                        }
                    },
                    "age_binning": {
                        "required": [
                            "hospitalizations",
                            "population"
                        ],
                        "properties": {
                            "hospitalizations": {
                                "items": {
                                    "type": "string"
                                }
                            },
                            "population": {
                                "items": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            },
            "region": {
                "type": "object",
                "required": [
                    "name",
                    "key",
                    "latitude",
                    "longitude",
                    "elevation",
                    "area",
                    "population",
                    "open_street_maps",
                    "noaa_station",
                    "noaa_distance"
                ],
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "key": {
                        "type": "string"
                    },
                    "latitude": {
                        "type": "number"
                    },
                    "longitude": {
                        "type": "number"
                    },
                    "elevation": {
                        "type": "number"
                    },
                    "area": {
                        "required": [
                            "total",
                            "rural",
                            "urban"
                        ],
                        "properties": {
                            "total": {
                                "type": "number"
                            },
                            "rural": {
                                "type": "number"
                            },
                            "urban": {
                                "type": "number"
                            }
                        }
                    },
                    "population": {
                        "required": [
                            "total",
                            "male",
                            "female",
                            "age",
                            "rural",
                            "urban"
                        ],
                        "properties": {
                            "total": {
                                "type": "integer"
                            },
                            "male": {
                                "type": "integer"
                            },
                            "female": {
                                "type": "integer"
                            },
                            "age": {
                                "items": {
                                    "type": "integer"
                                }
                            },
                            "rural": {
                                "type": "integer"
                            },
                            "urban": {
                                "type": "integer"
                            }
                        }
                    },
                    "open_street_maps": {
                        "type": "integer"
                    },
                    "noaa_station": {
                        "type": "integer"
                    },
                    "noaa_distance": {
                        "type": "number"
                    }
                }
            },
            "evolution": {
                "patternProperties": {
                    "(date)": {
                        "properties": {
                            "hospitalizations": {
                                "required": [
                                    "hospitalized",
                                    "intensive_care",
                                    "ventilator"
                                ],
                                "properties": {
                                    "hospitalized": {
                                        "required": [
                                            "new",
                                            "total",
                                            "current"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "type": ["array", "null"],
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "current": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "intensive_care": {
                                        "required": [
                                            "new",
                                            "total",
                                            "current"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "type": "array",
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "current": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "ventilator": {
                                        "required": [
                                            "new",
                                            "total",
                                            "current"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": ["integer", "null"]
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "current": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "epidemiology": {
                                "required": [
                                    "confirmed",
                                    "deceased",
                                    "recovered",
                                    "tested"
                                ],
                                "properties": {
                                    "confirmed": {
                                        "required": [
                                            "new",
                                            "total"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "deceased": {
                                        "required": [
                                            "new",
                                            "total"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "recovered": {
                                        "required": [
                                            "new",
                                            "total"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    },
                                    "tested": {
                                        "required": [
                                            "new",
                                            "total"
                                        ],
                                        "properties": {
                                            "new": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            },
                                            "total": {
                                                "required": [
                                                    "all",
                                                    "male",
                                                    "female",
                                                    "age"
                                                ],
                                                "properties": {
                                                    "all": {
                                                        "type": "integer"
                                                    },
                                                    "male": {
                                                        "type": "integer"
                                                    },
                                                    "female": {
                                                        "type": "integer"
                                                    },
                                                    "age": {
                                                        "items": {
                                                            "type": "integer"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            "weather": {
                                "required": [
                                    "temperature",
                                    "rainfall",
                                    "snowfall",
                                    "dew_point",
                                    "relative_humidity"
                                ],
                                "properties": {
                                    "temperature": {
                                        "required": [
                                            "average",
                                            "min",
                                            "max"
                                        ],
                                        "properties": {
                                            "average": {
                                                "type": "number"
                                            },
                                            "min": {
                                                "type": "number"
                                            },
                                            "max": {
                                                "type": "number"
                                            }
                                        }
                                    },
                                    "rainfall": {
                                        "type": "number"
                                    },
                                    "snowfall": {
                                        "type": "number"
                                    },
                                    "dew_point": {
                                        "type": "number"
                                    },
                                    "relative_humidity": {
                                        "type": "number"
                                    }
                                }
                            },
                            "government_response": {
                                "required": [
                                    "school_closing",
                                    "workplace_closing",
                                    "cancel_public_events",
                                    "restrictions_on_gatherings",
                                    "public_transport_closing",
                                    "stay_at_home_requirements",
                                    "restrictions_on_internal_movement",
                                    "international_travel_controls",
                                    "income_support",
                                    "debt_relief",
                                    "fiscal_measures",
                                    "international_support",
                                    "public_information_campaigns",
                                    "testing_policy",
                                    "contact_tracing",
                                    "emergency_investment_in_healthcare",
                                    "investment_in_vaccines",
                                    "stringency_index"
                                ],
                                "properties": {
                                    "school_closing": {
                                        "type": "integer"
                                    },
                                    "workplace_closing": {
                                        "type": "integer"
                                    },
                                    "cancel_public_events": {
                                        "type": "integer"
                                    },
                                    "restrictions_on_gatherings": {
                                        "type": "integer"
                                    },
                                    "public_transport_closing": {
                                        "type": "integer"
                                    },
                                    "stay_at_home_requirements": {
                                        "type": "integer"
                                    },
                                    "restrictions_on_internal_movement": {
                                        "type": "integer"
                                    },
                                    "international_travel_controls": {
                                        "type": "integer"
                                    },
                                    "income_support": {
                                        "type": "integer"
                                    },
                                    "debt_relief": {
                                        "type": "integer"
                                    },
                                    "fiscal_measures": {
                                        "type": "integer"
                                    },
                                    "international_support": {
                                        "type": "integer"
                                    },
                                    "public_information_campaigns": {
                                        "type": "integer"
                                    },
                                    "testing_policy": {
                                        "type": "integer"
                                    },
                                    "contact_tracing": {
                                        "type": "integer"
                                    },
                                    "emergency_investment_in_healthcare": {
                                        "type": "integer"
                                    },
                                    "investment_in_vaccines": {
                                        "type": "integer"
                                    },
                                    "stringency_index": {
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    }
                }

            }
        }
    }

    if not filepath.exists():
        raise NotImplementedError(
            'The path is not exist')

    with open(filepath, 'r') as json_file:
        my_data_as_string = json_file.read()

    try:
        json.loads(my_data_as_string)
    except TypeError:
        raise NotImplementedError(
            'The file structure is not Json')

    json_file = json.loads(my_data_as_string)

    try:
        validate(instance=json_file, schema=standard_schema)
    except:
        raise NotImplementedError('The file dose not follow standard schema')

    return json_file


def cases_per_population_by_age(input_data):

    # transform age_bin from string into int
    def age_bin_into_number(age_bin):
        age_bin = [x.split('-') for x in age_bin]
        age_bin[-1] = [age_bin[-1][0]]
        for i in range(len(age_bin)):
            bin_len = len(age_bin[i])
            new_bin = []
            for j in range(bin_len):
                new_bin.append(int(age_bin[i][j]))

            age_bin[i] = new_bin
        return age_bin

    # judge whether it's classified by age bins
    if not input_data['metadata']['age_binning']['hospitalizations']:
        raise NotImplementedError(
            'confirmed cases are not broken down into age groups')

    # transform the string age bins into int
    age_hospital = input_data['metadata']['age_binning']['hospitalizations']
    age_population = input_data['metadata']['age_binning']['population']
    age_hospital_int = age_bin_into_number(age_hospital)
    age_population_int = age_bin_into_number(age_population)
    age_hospital_flatten = [x for j in age_hospital_int for x in j]
    age_population_flatten = [x for j in age_population_int for x in j]

    if age_hospital_int != age_population_int:
        print('age ranges of hospitalization and population are not equal')

        if not (set(age_population_flatten) < set(age_hospital_flatten)) \
                and not (set(age_population_flatten) > set(age_hospital_flatten)):

            raise NotImplementedError(
                'Ages bins are not equal and can not rebin'
            )
        else:
            print('Aga bins can be rebined')

    age_bin_num = len(age_hospital)
    date_list = list(input_data['evolution'].keys())
    total_age_bin_ratio = []

    for i in range(age_bin_num):
        temp_age_population = input_data['region']['population']['age'][i]
        temp_age_bin_ratio = []

        for date in date_list:
            confirmed_case = input_data['evolution'][date]['epidemiology']['confirmed']['total']['age'][i]
            ratio = confirmed_case / temp_age_population
            temp_date_tuple = (date, ratio)
            temp_age_bin_ratio.append(temp_date_tuple)

        total_age_bin_ratio.append(temp_age_bin_ratio)

    result = dict(zip(age_hospital, total_age_bin_ratio))

    return result


def hospital_vs_confirmed(input_data):
    ratio_list = []
    effective_date = []
    date_list = list(input_data['evolution'].keys())
    for date in date_list:

        # check whether the data is missing
        if not input_data['evolution'][date]['epidemiology']['confirmed']['new']['all'] or \
                not input_data['evolution'][date]['hospitalizations']['hospitalized']['new']['all']:
            continue

        # check whether denominator of the ratio is zero
        if input_data['evolution'][date]['epidemiology']['confirmed']['new']['all'] != 0:
            confirmed_case = input_data['evolution'][date]['epidemiology']['confirmed']['new']['all']
            admission_hospital = input_data['evolution'][date]['hospitalizations']['hospitalized']['new']['all']
            adm_conf_ratio = admission_hospital / confirmed_case
            effective_date.append(date)
            ratio_list.append(adm_conf_ratio)

    tar_tuple = (effective_date, ratio_list)
    return tar_tuple


def generate_data_plot_confirmed(input_data, sex='', max_age=None, status='total'):
    """
    At most one of sex or max_age allowed at a time.
    sex: only 'male' or 'female'
    max_age: sums all bins below this value, including the one it is in.
    status: 'new' or 'total' (default: 'total')
    """

    if sex and max_age:
        raise NotImplementedError(
            'At most one of sex or max_age allowed at a time.')

    if status not in ['new', 'total']:
        raise NotImplementedError(
            'Status is not valid, it should only be new or total')

    if sex:
        if sex not in ['male', 'female']:
            raise NotImplementedError(
                'Sex is not valid.')
        else:
            date_list = list(input_data['evolution'].keys())
            confirmed_case_by_sex = []
            for date in date_list:
                temp_date_cases = input_data['evolution'][date]['epidemiology']['confirmed'][status][sex]
                confirmed_case_by_sex.append(temp_date_cases)

            result = dict(zip(date_list, confirmed_case_by_sex))
            return result

    if max_age:
        if not(isinstance(max_age, int)):
            raise NotImplementedError(
                'Max age should be integer.')

        if max_age < 0:
            raise NotImplementedError(
                'Max age should not be negative.')

        date_list = list(input_data['evolution'].keys())

        def bins_num(age):
            age_bin = input_data['metadata']['age_binning']['hospitalizations'][0:-1]
            age_split = [x.split('-') for x in age_bin]
            bin_num = 1
            for i in range(len(age_bin)):
                up_bin = int(age_split[i][1])
                if age > up_bin:
                    bin_num += 1
            return bin_num

        bin_num = bins_num(max_age)
        confirmed_case_by_age = []

        for date in date_list:
            temp_date_cases = input_data['evolution'][date]['epidemiology']['confirmed'][status]['age'][0:bin_num]
            sum = 0

            for x in temp_date_cases:
                sum += x
            confirmed_case_by_age.append(sum)

        result = dict(zip(date_list, confirmed_case_by_age))
        return result


def create_confirmed_plot(input_data, sex=False, max_ages=[], status='total', save=True, show=True):

    if sex and max_ages != []:
        raise NotImplementedError(
            'At most one of sex or max_age allowed at a time')

    if status not in ['new', 'total']:
        raise NotImplementedError(
            'Status is not valid, it should only be new or total')

    fig = plt.figure(figsize=(10, 10))
    if sex:
        for sex in ['male', 'female']:
            confirm_data = generate_data_plot_confirmed(input_data, sex, max_age=None, status=status)
            x = list(confirm_data.keys())
            y = list(confirm_data.values())
            if sex == 'male':
                plt.plot(x, y, 'green', label='{' + status + '}' + '{' + sex + '}')
            else:
                plt.plot(x, y, 'purple', label='{' + status + '}' + '{' + sex + '}')

    if max_ages != []:
        if not isinstance(max_ages, list):
            raise NotImplementedError(
                'Max_age should be a list')

        for age in max_ages:
            confirm_data = generate_data_plot_confirmed(input_data, max_age=age, status=status)
            x = list(confirm_data.keys())
            y = list(confirm_data.values())
            if 0 <= age <= 24:
                plt.plot(x, y, 'green', label='younger than 25')
            if 25 <= age <= 49:
                plt.plot(x, y, 'orange', label='younger than 50')
            if 50 <= age <= 74:
                plt.plot(x, y, 'purple', label='younger than 75')
            if age >= 75:
                plt.plot(x, y, 'pink', label='total')

    plt.legend()
    region = input_data['region']['name']
    fig.autofmt_xdate()  # To show dates nicely
    plt.xlabel("date")
    plt.ylabel("number of cases")
    plt.title("Confirmed cases " + input_data['region']['name'])
    # plt.legend(['0-24', '25-49', '50-74', '75-'])

    if show:
        plt.show()
    if save:
        plt.savefig(region + '_' + 'evoluation_cases_' + '{age}')


def compute_running_average(data, window):

    if not isinstance(data, list):
        raise NotImplementedError(
            'input data is not a list')

    if len(data) < 1:
        raise NotImplementedError(
            'The length of input data is too short')

    if not isinstance(window, int):
        raise NotImplementedError(
            'The size of window should be integer')

    if window > len(data):
        raise NotImplementedError(
            'The size of window is too large')

    if window % 2 == 0:
        raise NotImplementedError(
            'The window size should be odd number')

    if window < 0:
        raise NotImplementedError(
            'The window size should be positive')

    def calculate_average(input_list):
        res = []
        for val in input_list:
            if val is not None:
                res.append(val)
        result = sum(res) / len(res)

        # Truncate 3 decimals as shown in the example
        n = 3
        result = math.floor(result * 10 ** n) / (10 ** n)
        return result

    output = [None for _ in range(len(data))]

    half_window = int((window - 1) / 2)
    for x in range(len(data)):
        if half_window <= x <= len(data) - half_window - 1:
            window_list = data[x - half_window:x + half_window + 1]
            output[x] = calculate_average(window_list)
    return output


def simple_derivative(data):

    if not isinstance(data, list):
        raise NotImplementedError(
            'input data is not a list')

    if len(data) < 1:
        raise NotImplementedError(
            'The input data should not be empty' )

    output = [None for _ in data]

    for x in range(len(data)):
        if x >= 1 and data[x] is not None:
            if data[x - 1] is not None:
                output[x] = data[x] - data[x - 1]

    return output


def count_high_rain_low_tests_days(input_data):

    rainfall_list = []
    test_list = []
    date_list = list(input_data['evolution'].keys())

    for date in date_list:
        temp_date_rain = input_data['evolution'][date]['weather']['rainfall']
        rainfall_list.append(temp_date_rain)

        temp_date_test = input_data['evolution'][date]['epidemiology']['tested']['new']['all']
        test_list.append(temp_date_test)

    test_smoothed = compute_running_average(test_list, 7)

    rainfall_derivative = simple_derivative(rainfall_list)
    test_derivative = simple_derivative(test_smoothed)

    effect_days = 0
    rain_increase_day = 0

    for i in range(len(rainfall_list)):
        if rainfall_derivative[i] is not None and rainfall_derivative[i] > 0:
            rain_increase_day += 1

            if test_derivative[i] is not None and test_derivative[i] < 0:
                effect_days += 1

    effective_ratio = effect_days/rain_increase_day

    return effective_ratio



# -*- coding: utf-8 -*-

import numpy as np


def to_message(low, high, value):
    assert any(np.shape(arr) == np.shape(value) for arr in (low, high, value)) or np.shape(low) == np.shape(high) == np.shape(value[0:2])


    try:
        try:
            crnt_trial_num = value[2]
            crnt_trial_time = value[3]
        except IndexError:
            crnt_trial_num = 0
            crnt_trial_time = 0
            

        # convert numpy arrays to lists as they can not be json serialized
        try:
            low = low.tolist()
            high = high.tolist()
            value = value.tolist()
        except:
            pass
        message = [{'min': low[0], 'max': high[0], 'value': value[0],'crnt_trial_num':crnt_trial_num, 'crnt_trial_time':crnt_trial_time}
                 ,{'min': low[1], 'max': high[1], 'value': value[1]}
                 ]

#        return [{'min': low[i], 'max': high[i], 'value': value[i], 'crnt_tr_time':crnt_tr_time} for i in range(len(low))]
        return message 

    except TypeError:

        # convert numpy types to native types as they can not be json
        # serialized
        try:
            low = low.item()
        except:
            pass

        try:
            high = high.item()
        except:
            pass

        try:
            value = value.item()
        except:
            pass

        return [{'min': low, 'max': high, 'value': value}]

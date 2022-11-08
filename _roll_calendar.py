import argparse

from sysinit.futures.rollcalendars_from_arcticprices_to_csv import build_and_write_roll_calendar
from sysproduction.data.prices import get_valid_instrument_code_from_user

parser = argparse.ArgumentParser(
    prog = 'Roll calendar from Arctic prices',
    description = 'Generates new roll calendars from prices and stores in a temporary directory.'
)

parser.add_argument('-i', '--instrument')      # option that takes a value
parser.add_argument('-o', '--output')
args = parser.parse_args()

if args.instrument:
    instrument_code = args.instrument
    check_before_writing = False
else:
    instrument_code = get_valid_instrument_code_from_user(source="single")
    check_before_writing = True
if args.output:
    output_datapath=args.output
else:
    output_datapath="/Users/zinakaye/Documents/Trading/pysystemtrade/tmp/roll_calendars"

## MODIFY DATAPATH IF REQUIRED
# build_and_write_roll_calendar(instrument_code, output_datapath=arg_not_supplied)
build_and_write_roll_calendar(instrument_code, output_datapath=output_datapath, check_before_writing=check_before_writing)
print("Wrote %s roll calendar to %s/%s.csv." % (instrument_code, output_datapath, instrument_code))

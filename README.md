# Mapper
A label mapper that finds all events from an event log and provides a mapping gui to map the events from the event log 
to the activities in a process model. 

**Until now only functionalities for .xes event logs and dcr graphs process models are implemented**


## Getting Started

To run the tools, you need to install python3-tk

e.g. Ubuntu:
```
sudo apt-get install python3-tk
```
### Prerequisites
One important prerequisite is the pm4py module to read the event log. Therefore follow the instructions at 
[the Project page](http://pm4py.org/).
An easy way to get prerequisites might be using the makefile

```
make init
```

Another way if you have setuptools installed is to run setup.py or 'make install' if available:
```
python setup.py install
//
make install
```

### Running the Demo
Execute the program with one of the following command
1. ```make run```
2. ```python -m label-mapper```
3.  ```python label_mapper.py```

If you use one of these the Gui will pop up twice, once to ask for paths and then to map all the events.

If you want to skip searching for a path in a filedialog, you can provide three positional commandline arguments 
**Usage**:
```
python -m label_mapper [<log_path> <model_path> <output_path>]
python label_mapper.py [<log_path> <model_path> <output_path>]
```

## Contributing

Please read [CONTRIBUTING](Contributing.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Sebastian Dunzer** - *Initial work & Owner*
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details






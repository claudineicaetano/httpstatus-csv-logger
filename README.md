# HTTP Status CSV Logger
A Python script that reads CPFs from an `input.csv` file, makes POST requests to a REST endpoint, and logs the resulting HTTP status code in an `output.csv` file. Ideal for tracking the processing of CPFs and verifying the success or failure of requests via HTTP status codes.


## Features

- Reads CPFs from a CSV file.
- Sends POST requests with CPF data to a REST API.
- Logs HTTP status codes (200, 204, etc.) into an output CSV.
- Supports proxy and authentication setup.

## Prerequisites

- Python 3.x
- Install the required libraries:

    ```bash
    pip install requests
    ```

## How to Use

Clone the repository:

```bash
git clone https://github.com/claudineicaetano/httpstatus-csv-logger.git
cd httpstatus-csv-logger
```

Configure your endpoint, proxy, and authentication details in the script.

Prepare an `input.csv` file with a column named `cpf` containing CPF numbers.

Run the script:

```bash
python httpstatus_csv_logger.py
```

The HTTP status results will be saved in `output.csv` in the format: `cpf, httpstatus`.

## File Structure

```plaintext
.
├── httpstatus_csv_logger.py         # Main script to send POST requests and log HTTP status
├── input.csv         # Input file with CPF numbers
└── output.csv        # Output file with logged HTTP status codes
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more details.

### Summary of the GPL-3.0 License

- **Freedom to Use**: You can use the software for any purpose.
- **Freedom to Study and Modify**: You can study how the program works, and change it to make it do what you wish. Access to the source code is a precondition for this.
- **Freedom to Distribute Copies**: You can redistribute copies of the original program so you can help others.
- **Freedom to Distribute Modified Versions**: You can distribute copies of your modified versions to others. By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

For a detailed explanation of the GPL-3.0 license, please refer to the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).


---

Created with ❤️ by [claudineicaetano](https://github.com/claudineicaetano)

_"Freedom" is not a freedom if you don't feel free. My requirement to participate in projects: challenge, know-how and counterparty. Live long and prosper!_

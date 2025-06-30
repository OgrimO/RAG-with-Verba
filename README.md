Here is an implementation of RAG by using [Verba](https://pypi.org/project/goldenverba/)

# How to deploy with pip

`Python >=3.10.0`

1. **Initialize a new Python Environment**

```
python3 -m virtualenv venv
```

2. **Install Verba**

```
pip install goldenverba
```

3. **Launch Verba**

```
verba start
```

> You can specify the --port and --host via flags

4. **Access Verba**

```
Visit localhost:8000
```

5. **Create .env file and add environment variables**

# How to build from Source

1. **Clone the Verba repos**

```
git clone https://github.com/weaviate/Verba.git
```

2. **Initialize a new Python Environment**

```
python3 -m virtualenv venv
```

3. **Install Verba**

```
pip install -e .
```

4. **Launch Verba**

```
verba start
```

> You can specify the --port and --host via flags

5. **Access Verba**

```
Visit localhost:8000
```
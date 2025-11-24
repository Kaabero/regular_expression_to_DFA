#!/bin/bash

( cd UI && npm run dev ) &

cd Compiler && poetry run invoke start
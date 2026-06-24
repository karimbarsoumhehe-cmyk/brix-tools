@echo off
title Setup Tool Brix

echo ==================================
echo   Installation des dependances
echo ==================================
echo.

pip install --upgrade pip

echo.
echo Installation des modules...
pip install -r requirements.txt

echo.
echo ==================================
echo Installation terminee !
echo ==================================
echo.
pause
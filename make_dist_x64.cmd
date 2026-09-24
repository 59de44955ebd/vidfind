@echo off
setlocal EnableDelayedExpansion
cd /d %~dp0

:: config
set APP_NAME=vidfind
set ICON=app.ico
set APP_DIR=%CD%\dist\%APP_NAME%\
set DATA_DIR=data

call :cleanup
call :run_pyinstaller
call :copy_resources
call :optimize
call :create_7z

echo.
echo ****************************************
echo Done.
echo ****************************************
echo.
pause

endlocal
goto :eof


:cleanup
mkdir dist 2>nul
rmdir /s /q "dist\%APP_NAME%" 2>nul
del "dist\%APP_NAME%-x64.7z" 2>nul
exit /B


:run_pyinstaller
echo.
echo ****************************************
echo Running pyinstaller...
echo ****************************************

set PYTHONPATH=src
pyinstaller --noupx -n "%APP_NAME%" -i %ICON% -D "src/main.py" --contents-directory %DATA_DIR%
exit /B


:copy_resources
echo.
echo ****************************************
echo Copying resources...
echo ****************************************
xcopy /e "src\sniffer" "dist\%APP_NAME%\%DATA_DIR%\sniffer\" >nul
copy "src\webview2\native\win-amd64\loader.dll" "dist\%APP_NAME%\%DATA_DIR%\"
copy "src\index.htm" "dist\%APP_NAME%\%DATA_DIR%\"
exit /B


:optimize
echo.
echo ****************************************
echo Optimizing dist folder...
echo ****************************************
del /q "dist\%APP_NAME%\%DATA_DIR%\api-ms-win-*.dll"
del "dist\%APP_NAME%\%DATA_DIR%\VCRUNTIME140.dll"
del "dist\%APP_NAME%\%DATA_DIR%\ucrtbase.dll"
del "dist\%APP_NAME%\%DATA_DIR%\_bz2.pyd"
del "dist\%APP_NAME%\%DATA_DIR%\_lzma.pyd"
del "dist\%APP_NAME%\%DATA_DIR%\libcrypto-3.dll"
del "dist\%APP_NAME%\%DATA_DIR%\_socket.pyd"
del "dist\%APP_NAME%\%DATA_DIR%\unicodedata.pyd"
exit /B


:create_7z
if not exist "C:\Program Files\7-Zip\" (
	echo.
	echo ****************************************
	echo 7z.exe not found at default location, omitting .7z creation...
	echo ****************************************
	exit /B
)
echo.
echo ****************************************
echo Creating .7z archive...
echo ****************************************
cd dist
set PATH=C:\Program Files\7-Zip;%PATH%
7z a "%APP_NAME%-x64.7z" "%APP_NAME%\*"
cd ..
exit /B

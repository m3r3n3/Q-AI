const { app, BrowserWindow, screen } = require('electron');

function createWindow() {
    const mainScreen = screen.getPrimaryDisplay();
    const dimensions = mainScreen.size;

    const mainWindow = new BrowserWindow({
        width: dimensions.width,
        height: dimensions.height,
        webPreferences: {
            nodeIntegration: true
        }
    });

    mainWindow.loadFile('landing_page.html');

    // Open the DevTools (remove this in production)
    // mainWindow.webContents.openDevTools();
}

app.whenReady().then(createWindow);

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});

app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

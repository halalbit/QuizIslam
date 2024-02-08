import win32com.client

## Open Adobe Photoshop App programmatically and locate PSD file
psApp = win32com.client.Dispatch("Photoshop.Application")

psApp.Open(r"C:\Users\Super\Projet\QuizIslam\ressources\P1v.psd")
doc = psApp.Application.ActiveDocument

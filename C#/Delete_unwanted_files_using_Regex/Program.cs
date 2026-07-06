using System.Text.RegularExpressions;
using NLog;

namespace Delete_unwanted_files_using_Regex
{
    internal class Program
    {
        private static readonly Logger Logger = LogManager.GetCurrentClassLogger();

        private readonly string _parentFolderPath;
        private readonly Regex _fileNamePattern;

        private Program(string parentFolderPath, string pattern)
        {
            pattern = pattern.Replace("\\\\", "\\");
            _parentFolderPath = parentFolderPath;
            _fileNamePattern = new Regex(pattern, RegexOptions.IgnoreCase | RegexOptions.Compiled);
        }

        static void Main(string[] args)
        {
            try
            {
                if (args.Length < 2)
                {
                    Logger.Warn("Missing required arguments.");
                    Logger.Info("Usage: Delete_unwanted_files_using_Regex <parentFolderPath> <fileNameRegex>");
                    Logger.Info("Example: Delete_unwanted_files_using_Regex C:\\Temp \"\\.(tmp|bak)$\"");
                    return;
                }

                Logger.Info("Application started.");
                var program = new Program(args[0], args[1]);
                program.Run();
                Logger.Info("Application finished.");
            }
            catch (Exception ex)
            {
                Logger.Fatal(ex, "Unhandled exception.");
                throw;
            }
            finally
            {
                LogManager.Shutdown();
            }
        }

        private void Run()
        {
            if (!Directory.Exists(_parentFolderPath))
            {
                Logger.Warn("Folder not found: {FolderPath}", _parentFolderPath);
                return;
            }

            Logger.Info("Scanning folder: {FolderPath}", _parentFolderPath);
            Logger.Info("File name pattern: {Pattern}", _fileNamePattern);
            ProcessDirectory(_parentFolderPath);
        }

        private void ProcessDirectory(string directoryPath)
        {
            Logger.Debug("Entering directory: {DirectoryPath}", directoryPath);

            foreach (string filePath in Directory.EnumerateFiles(directoryPath))
            {
                ProcessFile(filePath);
            }

            foreach (string subDirectoryPath in Directory.EnumerateDirectories(directoryPath))
            {
                ProcessDirectory(subDirectoryPath);
            }
        }

        private void ProcessFile(string filePath)
        {
            string fileName = Path.GetFileName(filePath);

            if (!_fileNamePattern.IsMatch(fileName))
            {
                Logger.Trace("Skipped (no match): {FilePath}", filePath);
                return;
            }

            try
            {
                File.Delete(filePath);
                Logger.Info("Deleted: {FilePath}", filePath);
            }
            catch (Exception ex)
            {
                Logger.Error(ex, "Failed to delete: {FilePath}", filePath);
            }
        }
    }
}

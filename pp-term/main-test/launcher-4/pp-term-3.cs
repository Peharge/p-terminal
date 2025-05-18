/*
   Englisch | Peharge: This source code is released under the MIT License.

   Usage Rights:
   The source code may be copied, modified, and adapted to individual requirements.
   Users are permitted to use this code in their own projects, both for private and commercial purposes.
   However, it is recommended to modify the code only if you have sufficient programming knowledge,
   as changes could cause unintended errors or security risks.

   Dependencies and Additional Frameworks:
   The code relies on the use of various frameworks and executes additional files.
   Some of these files may automatically install further dependencies required for functionality.
   It is strongly recommended to perform installation and configuration in an isolated environment
   (e.g., a virtual environment) to avoid potential conflicts with existing software installations.

   Disclaimer:
   Use of the code is entirely at your own risk.
   Peharge assumes no liability for damages, data loss, system errors, or other issues
   that may arise directly or indirectly from the use, modification, or redistribution of the code.

   Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.
*/

/*
   Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.

   Nutzungsrechte:
   Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
   Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
   Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
   da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.

   Abhängigkeiten und zusätzliche Frameworks:
   Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
   Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
   Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
   um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.

   Haftungsausschluss:
   Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
   Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
   die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.

   Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.
*/

/*
   Français | Peharge: Ce code source est publié sous la licence MIT.

   Droits d'utilisation:
   Le code source peut être copié, édité et adapté aux besoins individuels.
   Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
   Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
   car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.

   Dépendances et frameworks supplémentaires:
   Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
   Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
   Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
   pour éviter d'éventuels conflits avec les installations de logiciels existantes.

   Clause de non-responsabilité:
   L'utilisation du code est entièrement à vos propres risques.
   Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
   pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.

   Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.
*/

using System;
using System.Diagnostics;
using System.IO;
using System.Text.Json;
using System.Text.Json.Nodes;

namespace PTerminal
{
    /// <summary>
    /// Manages a custom Windows Terminal profile and launches the terminal with a specified .bat script.
    /// </summary>
    internal static class Program
    {
        // Configuration constants
        private const string ProfileName = "PP-Terminal";
        private const string TabTitle = "PP-Term";
        private const string ColorScheme = "p-term";
        private const string FontFace = "FiraCode Nerd Font";
        private const string ProfileGuid = "{a9716167-e115-4217-907b-7a6ec5577ff8}";
        private const bool Hidden = false;

        // Resolve special folders
        private static readonly string UserProfile = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
        private static readonly string LocalAppData = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);

        // Paths
        private static readonly string BatPath = Path.Combine(UserProfile, "p-terminal", "pp-term", "run-pp-term-fast.bat");
        private static readonly string StartingDirectory = Path.Combine(UserProfile, "p-terminal", "pp-term");
        private static readonly string IconPath = Path.Combine(UserProfile, "p-terminal", "icons", "p-term-logo-5.png");
        private static readonly string SettingsPath = Path.Combine(LocalAppData,
            "Packages", "Microsoft.WindowsTerminal_8wekyb3d8bbwe", "LocalState", "settings.json");

        private static void Main()
        {
            try
            {
                var settings = LoadOrCreateSettings(SettingsPath);
                EnsureProfile(settings);
                SaveSettings(SettingsPath, settings);
                LaunchWindowsTerminal();
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine($"[Error] {ex.GetType().Name}: {ex.Message}");
            }
        }

        private static JsonObject LoadOrCreateSettings(string path)
        {
            if (File.Exists(path))
            {
                var jsonText = File.ReadAllText(path);
                return JsonNode.Parse(jsonText)?.AsObject() ?? new JsonObject();
            }
            return new JsonObject();
        }

        private static void EnsureProfile(JsonObject settings)
        {
            // Ensure "profiles" object exists
            if (!settings.TryGetPropertyValue("profiles", out JsonNode profilesNode) || profilesNode is not JsonObject profiles)
            {
                profiles = new JsonObject();
                settings["profiles"] = profiles;
            }

            // Ensure "list" array exists
            if (!profiles.TryGetPropertyValue("list", out JsonNode listNode) || listNode is not JsonArray list)
            {
                list = new JsonArray();
                profiles["list"] = list;
            }

            // Add profile if not exists
            if (!ProfileExists(list))
            {
                var newProfile = new JsonObject
                {
                    ["name"] = ProfileName,
                    ["guid"] = ProfileGuid,
                    ["hidden"] = Hidden,
                    ["tabTitle"] = TabTitle,
                    ["commandline"] = BatPath,
                    ["startingDirectory"] = StartingDirectory,
                    ["icon"] = IconPath,
                    ["colorScheme"] = ColorScheme,
                    ["font"] = new JsonObject { ["face"] = FontFace }
                };
                list.Add(newProfile);
            }
        }

        private static bool ProfileExists(JsonArray list)
        {
            foreach (var node in list)
            {
                if (node is JsonObject obj &&
                    obj.TryGetPropertyValue("name", out JsonNode nameNode) &&
                    nameNode?.GetValue<string>() == ProfileName)
                {
                    return true;
                }
            }
            return false;
        }

        private static void SaveSettings(string path, JsonObject settings)
        {
            var options = new JsonSerializerOptions { WriteIndented = true };
            var updatedJson = JsonSerializer.Serialize(settings, options);
            File.WriteAllText(path, updatedJson);
        }

        private static void LaunchWindowsTerminal()
        {
            // Prepare arguments: select profile, then launch .bat
            var arguments = $"-p \"{ProfileName}\" cmd /k \"call \"{BatPath}\"\"";

            var psi = new ProcessStartInfo
            {
                FileName = "wt.exe",
                Arguments = arguments,
                UseShellExecute = true,
                CreateNoWindow = false
            };

            Process.Start(psi);
        }
    }
}

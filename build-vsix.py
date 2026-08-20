#!/usr/bin/env python3
"""Build a valid .vsix for this extension.

vsce's own packager produces an empty payload under recent Node versions here,
so this builds the package structure directly. A .vsix is a zip containing:
  extension.vsixmanifest   - the gallery manifest (root)
  [Content_Types].xml      - MIME map (root)
  extension/...            - the actual extension files
"""
import json
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

pkg = json.load(open("package.json"))
NAME = pkg["name"]
VERSION = pkg["version"]
PUBLISHER = pkg["publisher"]
ICON = pkg.get("icon")

# Files shipped inside extension/
ship = ["package.json", "README.md", "CHANGELOG.md", "LICENSE"]
for g in pkg.get("contributes", {}).get("grammars", []):
    ship.append(g["path"].lstrip("./"))
if ICON:
    ship.append(ICON)
for f in ship:
    assert os.path.isfile(f), f"MISSING {f}"

repo = pkg.get("repository", {})
repo_url = repo.get("url") if isinstance(repo, dict) else repo

icon_asset = (
    f'\n\t\t<Asset Type="Microsoft.VisualStudio.Services.Icons.Default" '
    f'Path="extension/{ICON}" Addressable="true" />' if ICON else ""
)

manifest = f'''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
	<Metadata>
		<Identity Language="en-US" Id="{NAME}" Version="{VERSION}" Publisher="{PUBLISHER}" />
		<DisplayName>{pkg["displayName"]}</DisplayName>
		<Description xml:space="preserve">{pkg["description"]}</Description>
		<Tags>{",".join(pkg.get("keywords", []))}</Tags>
		<Categories>{",".join(pkg.get("categories", []))}</Categories>
		<GalleryFlags>Public</GalleryFlags>
		<Properties>
			<Property Id="Microsoft.VisualStudio.Code.Engine" Value="{pkg["engines"]["vscode"]}" />
			<Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="ui,workspace,web" />
			<Property Id="Microsoft.VisualStudio.Services.Links.Source" Value="{repo_url}" />
			<Property Id="Microsoft.VisualStudio.Services.Links.GitHub" Value="{repo_url}" />
			<Property Id="Microsoft.VisualStudio.Services.Branding.Color" Value="#26383d" />
			<Property Id="Microsoft.VisualStudio.Services.Branding.Theme" Value="dark" />
			<Property Id="Microsoft.VisualStudio.Services.GitHubFlavoredMarkdown" Value="true" />
			<Property Id="Microsoft.VisualStudio.Services.Content.Pricing" Value="Free"/>
		</Properties>
	</Metadata>
	<Installation>
		<InstallationTarget Id="Microsoft.VisualStudio.Code"/>
	</Installation>
	<Dependencies/>
	<Assets>
		<Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
		<Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true" />
		<Asset Type="Microsoft.VisualStudio.Services.Content.Changelog" Path="extension/CHANGELOG.md" Addressable="true" />
		<Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE" Addressable="true" />{icon_asset}
	</Assets>
</PackageManifest>
'''

content_types = '''<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
	<Default Extension="json" ContentType="application/json"/>
	<Default Extension="md" ContentType="text/markdown"/>
	<Default Extension="png" ContentType="image/png"/>
	<Default Extension="vsixmanifest" ContentType="text/xml"/>
	<Override PartName="/extension/LICENSE" ContentType="text/plain"/>
</Types>
'''

out = f"{NAME}-{VERSION}.vsix"
if os.path.exists(out):
    os.remove(out)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("extension.vsixmanifest", manifest)
    z.writestr("[Content_Types].xml", content_types)
    for f in ship:
        z.write(f, f"extension/{f}")

with zipfile.ZipFile(out) as z:
    names = z.namelist()
assert "extension/package.json" in names
print(f"Built {out} ({os.path.getsize(out)} bytes, {len(names)} entries)")
for n in names:
    print("  ", n)

import mujoco
import os
import xml.etree.ElementTree as ET

# --- Method 1: Get name from an XML string ---

xml_string = """
<mujoco model="my_project_from_string">
  <worldbody>
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="1 1 0.1" rgba=".9 0 0 1"/>
    <body pos="0 0 1">
      <joint type="free"/>
      <geom type="box" size=".1 .2 .3" rgba="0 .9 0 1"/>
    </body>
  </worldbody>
</mujoco>
"""

# Parse the XML string
try:
    root = ET.fromstring(xml_string)
    project_name_from_string = root.get('model')
    print(f"Successfully retrieved project name from XML string: '{project_name_from_string}'")

    # You can now load the model into MuJoCo as usual
    model_from_string = mujoco.MjModel.from_xml_string(xml_string)
    print("Model loaded successfully from string.")

except ET.ParseError as e:
    print(f"Error parsing XML string: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


print("\n" + "-"*30 + "\n")


# --- Method 2: Get name from an XML file ---

xml_path = "temp_model.xml"
with open(xml_path, "w") as f:
    f.write(xml_string.replace("my_project_from_string", "my_project_from_file"))

print(f"Working with temporary XML file: {xml_path}")

# Parse the XML file
try:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    project_name_from_file = root.get('model')
    print(f"Successfully retrieved project name from XML file: '{project_name_from_file}'")

    # You can now load the model into MuJoCo
    model_from_file = mujoco.MjModel.from_xml_path(xml_path)
    print("Model loaded successfully from file.")

except ET.ParseError as e:
    print(f"Error parsing XML file: {e}")
except FileNotFoundError:
    print(f"Error: The file '{xml_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Clean up the temporary file
    if os.path.exists(xml_path):
        os.remove(xml_path)
        print(f"\nTemporary file '{xml_path}' removed.")

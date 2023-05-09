# lib parser
import argparse
# lib logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s %(levelname)s] --> %(module)s: %(message)s'
)

import re
import os
import glob
import shutil

def Read_argument():
    parser = argparse.ArgumentParser(description="write args")
    parser.add_argument("-m", "--module", help="Choose module", nargs='+', default=None)
    return parser.parse_args()

class mTest():

    variable = "Variable.py"
    if os.path.exists(variable):
        exec(open(variable).read())

class mRunTool():
    def __init__(self, module):
        self.MODULE = module
        self.mTest = mTest()
        self.status = "FAIL"
        print("")

    def LetStart(self):
        logging.info(f"*************************************")
        logging.info(f"Start generate plugin {self.MODULE}")
        logging.info(f"*************************************")

    def LetEnd(self):
        logging.info(f"*************************************")
        logging.info(f"End generate plugin {self.MODULE} ====> {self.status}")
        logging.info(f"*************************************\n")
    
    def Copy_Module(self):
        shutil.copytree('Template_Emty', f'Output/{self.MODULE}_HuLa')

    def Replace_Variable(self):
        with open("Template/META-INF/MANIFEST.MF","r") as file:
            data = file.read()
            data = data.replace("@MODULE@",self.MODULE )
            data = data.replace("@VERSION_MAJOR@",self.mTest.VERSION_MAJOR )
            data = data.replace("@VERSION_MINOR@",self.mTest.VERSION_MINOR  )
            data = data.replace("@VERSION_PATCH@",self.mTest.VERSION_PATCH )
            data = data.replace("@RELEASE_TYPE@",self.mTest.RELEASE_TYPE )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MAJOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MAJOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MINOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MINOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_PATCH@",self.mTest.AUTOSAR_RELEASE_VERSION_PATCH )
            data = data.replace("@ASC_AUTOSAR_VERSION@",self.mTest.ASC_AUTOSAR_VERSION )
            data = data.replace("@AUTOSAR_VERSION@",self.mTest.AUTOSAR_VERSION )
            data = data.replace("@COMPANY_NAME@",self.mTest.COMPANY_NAME )
            data = data.replace("@VENDOR_ID@",self.mTest.VENDOR_ID )
            data = data.replace("@MANDATORY_T@",self.mTest.MANDATORY_T )
            data = data.replace("@INSTANCE_ID@",self.mTest.INSTANCE_ID )
            data = data.replace("@RESOURCE_PACKAGE@",self.mTest.RESOURCE_PACKAGE )
            data = data.replace("@TARGET_ARCHITECTURE@",self.mTest.TARGET_ARCHITECTURE )
            data = data.replace("@SILICON_NAME@",self.mTest.SILICON_NAME )
            data = data.replace("@RELEASE_NAME@",self.mTest.RELEASE_NAME )
            data = data.replace("@COPYRIGHT@",self.mTest.COPYRIGHT )
            with open(f'Output/{self.MODULE}_HuLa/META-INF/MANIFEST.MF',"w+") as outfile:
                outfile.write(data)

        with open("Template/anchors.xml","r") as file:
            data = file.read()
            data = data.replace("@MODULE@",self.MODULE )
            data = data.replace("@VERSION_MAJOR@",self.mTest.VERSION_MAJOR )
            data = data.replace("@VERSION_MINOR@",self.mTest.VERSION_MINOR  )
            data = data.replace("@VERSION_PATCH@",self.mTest.VERSION_PATCH )
            data = data.replace("@RELEASE_TYPE@",self.mTest.RELEASE_TYPE )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MAJOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MAJOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MINOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MINOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_PATCH@",self.mTest.AUTOSAR_RELEASE_VERSION_PATCH )
            data = data.replace("@ASC_AUTOSAR_VERSION@",self.mTest.ASC_AUTOSAR_VERSION )
            data = data.replace("@AUTOSAR_VERSION@",self.mTest.AUTOSAR_VERSION )
            data = data.replace("@COMPANY_NAME@",self.mTest.COMPANY_NAME )
            data = data.replace("@VENDOR_ID@",self.mTest.VENDOR_ID )
            data = data.replace("@MANDATORY_T@",self.mTest.MANDATORY_T )
            data = data.replace("@INSTANCE_ID@",self.mTest.INSTANCE_ID )
            data = data.replace("@RESOURCE_PACKAGE@",self.mTest.RESOURCE_PACKAGE )
            data = data.replace("@TARGET_ARCHITECTURE@",self.mTest.TARGET_ARCHITECTURE )
            data = data.replace("@SILICON_NAME@",self.mTest.SILICON_NAME )
            data = data.replace("@RELEASE_NAME@",self.mTest.RELEASE_NAME )
            data = data.replace("@COPYRIGHT@",self.mTest.COPYRIGHT )
            with open(f'Output/{self.MODULE}_HuLa/anchors.xml',"w+") as outfile:
                outfile.write(data)

        with open("Template/ant_generator.xml","r") as file:
            data = file.read()
            data = data.replace("@MODULE@",self.MODULE )
            data = data.replace("@VERSION_MAJOR@",self.mTest.VERSION_MAJOR )
            data = data.replace("@VERSION_MINOR@",self.mTest.VERSION_MINOR  )
            data = data.replace("@VERSION_PATCH@",self.mTest.VERSION_PATCH )
            data = data.replace("@RELEASE_TYPE@",self.mTest.RELEASE_TYPE )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MAJOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MAJOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MINOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MINOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_PATCH@",self.mTest.AUTOSAR_RELEASE_VERSION_PATCH )
            data = data.replace("@ASC_AUTOSAR_VERSION@",self.mTest.ASC_AUTOSAR_VERSION )
            data = data.replace("@AUTOSAR_VERSION@",self.mTest.AUTOSAR_VERSION )
            data = data.replace("@COMPANY_NAME@",self.mTest.COMPANY_NAME )
            data = data.replace("@VENDOR_ID@",self.mTest.VENDOR_ID )
            data = data.replace("@MANDATORY_T@",self.mTest.MANDATORY_T )
            data = data.replace("@INSTANCE_ID@",self.mTest.INSTANCE_ID )
            data = data.replace("@RESOURCE_PACKAGE@",self.mTest.RESOURCE_PACKAGE )
            data = data.replace("@TARGET_ARCHITECTURE@",self.mTest.TARGET_ARCHITECTURE )
            data = data.replace("@SILICON_NAME@",self.mTest.SILICON_NAME )
            data = data.replace("@RELEASE_NAME@",self.mTest.RELEASE_NAME )
            data = data.replace("@COPYRIGHT@",self.mTest.COPYRIGHT )
            with open(f'Output/{self.MODULE}_HuLa/ant_generator.xml',"w+") as outfile:
                outfile.write(data)

        with open("Template/plugin.xml","r") as file:
            data = file.read()
            data = data.replace("@MODULE@",self.MODULE )
            data = data.replace("@VERSION_MAJOR@",self.mTest.VERSION_MAJOR )
            data = data.replace("@VERSION_MINOR@",self.mTest.VERSION_MINOR  )
            data = data.replace("@VERSION_PATCH@",self.mTest.VERSION_PATCH )
            data = data.replace("@RELEASE_TYPE@",self.mTest.RELEASE_TYPE )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MAJOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MAJOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_MINOR@",self.mTest.AUTOSAR_RELEASE_VERSION_MINOR )
            data = data.replace("@AUTOSAR_RELEASE_VERSION_PATCH@",self.mTest.AUTOSAR_RELEASE_VERSION_PATCH )
            data = data.replace("@ASC_AUTOSAR_VERSION@",self.mTest.ASC_AUTOSAR_VERSION )
            data = data.replace("@AUTOSAR_VERSION@",self.mTest.AUTOSAR_VERSION )
            data = data.replace("@COMPANY_NAME@",self.mTest.COMPANY_NAME )
            data = data.replace("@VENDOR_ID@",self.mTest.VENDOR_ID )
            data = data.replace("@MANDATORY_T@",self.mTest.MANDATORY_T )
            data = data.replace("@INSTANCE_ID@",self.mTest.INSTANCE_ID )
            data = data.replace("@RESOURCE_PACKAGE@",self.mTest.RESOURCE_PACKAGE )
            data = data.replace("@TARGET_ARCHITECTURE@",self.mTest.TARGET_ARCHITECTURE )
            data = data.replace("@SILICON_NAME@",self.mTest.SILICON_NAME )
            data = data.replace("@RELEASE_NAME@",self.mTest.RELEASE_NAME )
            data = data.replace("@COPYRIGHT@",self.mTest.COPYRIGHT )
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(data)

    def Remove_Block_Code(self):
        if(self.mTest.MULTI_INSTANCE == "No"):
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                data = file.read()
                matches = re.findall("(#START_REMOVE_MULTI_INSTANCE#.*?#END_REMOVE_MULTI_INSTANCE#)", data, re.DOTALL | re.MULTILINE)
                for match in matches:
                    data = data.replace(match, "")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(data)
        else:
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("#START_REMOVE_MULTI_INSTANCE#","")
                DataPlugin = DataPlugin.replace("#END_REMOVE_MULTI_INSTANCE#","")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(DataPlugin)

        if(self.MODULE == "Ecuc" or self.MODULE == "ecuc" or self.MODULE == "ECUC" or self.MODULE == "EcuC"):
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("#START_REMOVE_ECUC_POSTBUILD#","")
                DataPlugin = DataPlugin.replace("#END_REMOVE_ECUC_POSTBUILD#","")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(DataPlugin)
            os.makedirs(f'./Output/{self.MODULE}_HuLa/config',mode = 0o777,exist_ok= True)
            shutil.copyfile("Template/config/EcuC.xdm",f'Output/{self.MODULE}_HuLa/config/EcuC.xdm') 
            with open(f'Output/{self.MODULE}_HuLa/config/EcuC.xdm',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("@SILICON_NAME@",self.mTest.SILICON_NAME)
                DataPlugin = DataPlugin.replace("@MODULE@",self.MODULE)
            with open(f'Output/{self.MODULE}_HuLa/config/EcuC.xdm',"w+") as outfile:
                outfile.write(DataPlugin)
        else:
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                data = file.read()
                matches = re.findall("(#START_REMOVE_ECUC_POSTBUILD#.*?#END_REMOVE_ECUC_POSTBUILD#)", data, re.DOTALL | re.MULTILINE)
                for match in matches:
                    data = data.replace(match, "")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(data)
            

        if(self.MODULE == "Resource" or self.MODULE == "resource" or self.MODULE == "RESOURCE"):
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("#START_REMOVE_RESOURCE_SUPPORT#","")
                DataPlugin = DataPlugin.replace("#END_REMOVE_RESOURCE_SUPPORT#","")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(DataPlugin)
            os.makedirs(f'./Output/{self.MODULE}_HuLa/config',mode = 0o777,exist_ok= True)
            shutil.copyfile("Template/config/Resource.xdm",f'Output/{self.MODULE}_HuLa/config/Resource.xdm')
            shutil.copytree("Template/Resource", f'Output/{self.MODULE}_HuLa/Resource')
            with open(f'Output/{self.MODULE}_HuLa/config/Resource.xdm',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("@SILICON_NAME@",self.mTest.SILICON_NAME)
                DataPlugin = DataPlugin.replace("@MODULE@",self.MODULE)
            with open(f'Output/{self.MODULE}_HuLa/config/Resource.xdm',"w+") as outfile:
                outfile.write(DataPlugin)
        else:
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"r") as file:
                data = file.read()
                matches = re.findall("(#START_REMOVE_RESOURCE_SUPPORT#.*?#END_REMOVE_RESOURCE_SUPPORT#)", data, re.DOTALL | re.MULTILINE)
                for match in matches:
                    data = data.replace(match, "")
            with open(f'Output/{self.MODULE}_HuLa/plugin.xml',"w+") as outfile:
                outfile.write(data)
            

    def Copy_Template_Code(self):
        if(self.MODULE != "Resource" and self.MODULE != "resource" and self.MODULE != "RESOURCE" and self.MODULE != "Ecuc" and self.MODULE != "ecuc" and self.MODULE != "ECUC" and self.MODULE != "EcuC"):
            os.makedirs(f'./Output/{self.MODULE}_HuLa/config',mode = 0o777,exist_ok= True)
            shutil.copyfile("Template/config/Gpio.xdm",f'Output/{self.MODULE}_HuLa/config/{self.MODULE}.xdm')
            shutil.copytree("Template/generate_PB", f'Output/{self.MODULE}_HuLa/generate_PB')
            shutil.copytree("Template/generate_PC", f'Output/{self.MODULE}_HuLa/generate_PC')

            with open(f'Output/{self.MODULE}_HuLa/config/{self.MODULE}.xdm',"r") as file:
                DataPlugin = file.read()
                DataPlugin = DataPlugin.replace("@SILICON_NAME@",self.mTest.SILICON_NAME)
                DataPlugin = DataPlugin.replace("@MODULE@",self.MODULE)
            with open(f'Output/{self.MODULE}_HuLa/config/{self.MODULE}.xdm',"w+") as outfile:
                outfile.write(DataPlugin)

            

    def Start(self):
        self.LetStart()

        if os.path.exists(f'Output/{self.MODULE}_HuLa/META-INF/MANIFEST.MF'):
            shutil.rmtree(f'Output/{self.MODULE}_HuLa')

        self.Copy_Module()

        self.Replace_Variable()

        self.Remove_Block_Code()

        self.Copy_Template_Code()

        self.status= "SUCCESSED"
        self.LetEnd()

        

        
        
if __name__ == '__main__':
    Argument = Read_argument()
    logging.info("module = %s ",Argument.module[0])
    RunNew = mRunTool(Argument.module[0])
    RunNew.Start()
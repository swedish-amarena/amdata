% A short introduction to the MDCS way to store data
% N. Stenberg


# Introduction

The MDCS works as a storage point for all structured data and meta data
that is derrived from Swedish research on materials for Additive
manufacturing (AM).

The MDCS has two ways of interaction, the web interface and the Rest
API. A Rest API is basically a couple of dedicated web pages where information
can be exchanged as opposed to a "full" API where information exchange
is separated from the web server.

# Data structure of the MDCS

- Data is stored in a noSQL database (mongoDB). 
- Every post have a unique number.
- A post can be 
	- a BLOB (Binary Large OBject)
	- or an XML-string
- BLOB:s are typically pictures, documents, raw-files, etc.
- XML-strings are based on *templates*
- User input belong to user
- To make data accessible to all it must belong to a *workspace*
- To make *templates* accessible to all it must be made *global*

## The XML-string

The data is stored as a XML-string. The DB-post's keys are:

- **'id'**
	- the unique id-number for that specific post
- **'template'**
	- the unique id-number for the used template
- **'user_id'**
	- the user number
- **'title'**
	- the title for the post
- **'xml_content'**
	- the XML-string that is the actual information that is put into
      the fields of the template
- **'last_modification_date'**
	- just guess...


## The template

The template consists of several different fields that has been
defined by the user. The MDCS can handle a vast amount of templates
and the information of the templates. All information
regarding a specific dataset is avilable in the system. 

Templates can be created with the web interface or written externally
and uploaded. When entering data template fields are allowed to be
empty.

It is suggested that templates are made accessible globally. It is
also suggested just a handful of templates are in use and the contents
are based on consensus among the users.


An example of a Template:

```
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  	<xsd:element name="tDrag01" type="TRoot"/>
  
	<xsd:complexType name="TRoot">
		<xsd:sequence>
		  <xsd:element name="material" type="xsd:string"/>
		  <xsd:element name="blobid" type="xsd:string"/>
		  ...
		</xsd:sequence>
	</xsd:complexType>
</xsd:schema>
```
A longer Template as used by NIST is shown in the end of the document.


# Other nice functions in the MDCS

## Types

When creating templates base templates can be stored as *Types*


## Workspaces

By putting data posts in workspaces it is possible to control the
permissions to data.

It is however suggested that *global* workspaces are used to let all
scientists access the data: the AM-arena materials database is a tool
for collaboration.

## Administration

The administration part is an extended form of standard Django
admin. Check it out. It can be used to handle templates, workspaces,
files and such.




# Appendix A : An example of a template

```
<xsd:schema attributeFormDefault="unqualified" elementFormDefault="qualified"
	xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<!-- ================================================== -->
	<!-- =====  Element Declarations  -->
	<!-- ================================================== -->
	<xsd:element name="interDiffusion" type="Experiment"/>
	<!-- ================================================== -->
	<!-- =====  Complex Type Definitions  -->
	<!-- ================================================== -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  CatalogNumber  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="CatalogNumber">
		<xsd:sequence>
			<xsd:element name="id" type="xsd:string"/>
			<xsd:element name="catalogTitle" type="CatalogTitle"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  CatalogTitle  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="CatalogTitle">
		<xsd:sequence>
			<xsd:element name="name" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ChemicalElement  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="ChemicalElement">
		<xsd:annotation>
			<xsd:documentation>
				<div class="summary">
Allowed					<tt>ChemicalElementType</tt>
 values.				</div>
				<div class="description">
					<p>Modified from Chemical Markup Language. The periodic table (up to
            element number 118. In addition the following strings are allowed:</p>
				</div>
			</xsd:documentation>
		</xsd:annotation>
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="Ac"/>
			<xsd:enumeration value="Al"/>
			<xsd:enumeration value="Ag"/>
			<xsd:enumeration value="Am"/>
			<xsd:enumeration value="Ar"/>
			<xsd:enumeration value="As"/>
			<xsd:enumeration value="At"/>
			<xsd:enumeration value="Au"/>
			<xsd:enumeration value="B"/>
			<xsd:enumeration value="Ba"/>
			<xsd:enumeration value="Bh"/>
			<xsd:enumeration value="Bi"/>
			<xsd:enumeration value="Be"/>
			<xsd:enumeration value="Bk"/>
			<xsd:enumeration value="Br"/>
			<xsd:enumeration value="C"/>
			<xsd:enumeration value="Ca"/>
			<xsd:enumeration value="Cd"/>
			<xsd:enumeration value="Ce"/>
			<xsd:enumeration value="Cf"/>
			<xsd:enumeration value="Cl"/>
			<xsd:enumeration value="Cm"/>
			<xsd:enumeration value="Co"/>
			<xsd:enumeration value="Cr"/>
			<xsd:enumeration value="Cs"/>
			<xsd:enumeration value="Cu"/>
			<xsd:enumeration value="Db"/>
			<xsd:enumeration value="Dy"/>
			<xsd:enumeration value="Er"/>
			<xsd:enumeration value="Es"/>
			<xsd:enumeration value="Eu"/>
			<xsd:enumeration value="F"/>
			<xsd:enumeration value="Fe"/>
			<xsd:enumeration value="Fm"/>
			<xsd:enumeration value="Fr"/>
			<xsd:enumeration value="Ga"/>
			<xsd:enumeration value="Gd"/>
			<xsd:enumeration value="Ge"/>
			<xsd:enumeration value="H"/>
			<xsd:enumeration value="He"/>
			<xsd:enumeration value="Hf"/>
			<xsd:enumeration value="Hg"/>
			<xsd:enumeration value="Ho"/>
			<xsd:enumeration value="Hs"/>
			<xsd:enumeration value="I"/>
			<xsd:enumeration value="In"/>
			<xsd:enumeration value="Ir"/>
			<xsd:enumeration value="K"/>
			<xsd:enumeration value="Kr"/>
			<xsd:enumeration value="La"/>
			<xsd:enumeration value="Li"/>
			<xsd:enumeration value="Lr"/>
			<xsd:enumeration value="Lu"/>
			<xsd:enumeration value="Md"/>
			<xsd:enumeration value="Mg"/>
			<xsd:enumeration value="Mn"/>
			<xsd:enumeration value="Mo"/>
			<xsd:enumeration value="Mt"/>
			<xsd:enumeration value="N"/>
			<xsd:enumeration value="Na"/>
			<xsd:enumeration value="Nb"/>
			<xsd:enumeration value="Nd"/>
			<xsd:enumeration value="Ne"/>
			<xsd:enumeration value="Ni"/>
			<xsd:enumeration value="No"/>
			<xsd:enumeration value="Np"/>
			<xsd:enumeration value="O"/>
			<xsd:enumeration value="Os"/>
			<xsd:enumeration value="P"/>
			<xsd:enumeration value="Pa"/>
			<xsd:enumeration value="Pb"/>
			<xsd:enumeration value="Pd"/>
			<xsd:enumeration value="Pm"/>
			<xsd:enumeration value="Po"/>
			<xsd:enumeration value="Pr"/>
			<xsd:enumeration value="Pt"/>
			<xsd:enumeration value="Pu"/>
			<xsd:enumeration value="Ra"/>
			<xsd:enumeration value="Rb"/>
			<xsd:enumeration value="Re"/>
			<xsd:enumeration value="Rf"/>
			<xsd:enumeration value="Rh"/>
			<xsd:enumeration value="Rn"/>
			<xsd:enumeration value="Ru"/>
			<xsd:enumeration value="S"/>
			<xsd:enumeration value="Sb"/>
			<xsd:enumeration value="Sc"/>
			<xsd:enumeration value="Se"/>
			<xsd:enumeration value="Sg"/>
			<xsd:enumeration value="Si"/>
			<xsd:enumeration value="Sm"/>
			<xsd:enumeration value="Sn"/>
			<xsd:enumeration value="Sr"/>
			<xsd:enumeration value="Ta"/>
			<xsd:enumeration value="Tb"/>
			<xsd:enumeration value="Tc"/>
			<xsd:enumeration value="Te"/>
			<xsd:enumeration value="Th"/>
			<xsd:enumeration value="Ti"/>
			<xsd:enumeration value="Tl"/>
			<xsd:enumeration value="Tm"/>
			<xsd:enumeration value="U"/>
			<xsd:enumeration value="Uun"/>
			<xsd:enumeration value="Uuu"/>
			<xsd:enumeration value="Uub"/>
			<xsd:enumeration value="Uut"/>
			<xsd:enumeration value="Uuq"/>
			<xsd:enumeration value="Uup"/>
			<xsd:enumeration value="Uuh"/>
			<xsd:enumeration value="Uus"/>
			<xsd:enumeration value="Uuo"/>
			<xsd:enumeration value="V"/>
			<xsd:enumeration value="W"/>
			<xsd:enumeration value="Xe"/>
			<xsd:enumeration value="Y"/>
			<xsd:enumeration value="Yb"/>
			<xsd:enumeration value="Zn"/>
			<xsd:enumeration value="Zr"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ChemicalSubstance  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ChemicalSubstance">
		<xsd:sequence>
			<xsd:element name="chemicalFormula" type="xsd:string"/>
			<xsd:element name="name" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="catalogNumber"
				type="CatalogNumber"/>
			<xsd:element maxOccurs="unbounded" name="elements" type="ChemicalElement"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Citation (Requirement: Either Citation or DOI sufficient, can be both. TODO: Look for citation uml model to develop a schema -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="CitationType">
		<xsd:sequence>
			<xsd:element name="reference" type="xsd:string"/>
			<xsd:element name="doi" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Citation : Citation Required(Requirement: Either Citation or DOI sufficient, can be both. TODO: Look for citation uml model to develop a schema -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="CitationOnlyType">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="DOI" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Citation : DOI Required(Requirement: Either Citation or DOI sufficient, can be both. TODO: Look for citation uml model to develop a schema -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DOIOnlyType">
		<xsd:sequence> </xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Comments  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Comments">
		<xsd:sequence>
			<xsd:element name="resultType" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" name="comment" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Composition  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ConstituentType  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ConstituentsType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="constituent"
				type="ConstituentMaterial"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ConstituentElement  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ConstituentElement">
		<xsd:sequence>
			<xsd:element name="element" type="ChemicalElement"/>
			<xsd:element name="subscript" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ConstituentMaterial  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ConstituentMaterial">
		<xsd:sequence>
			<xsd:element name="element" type="ChemicalElement"/>
			<xsd:element name="quantity" type="xsd:string"/>
			<xsd:element minOccurs="0" name="purity" type="xsd:string"/>
			<xsd:element minOccurs="0" name="error" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  CrystalStructure  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="CrystalStructure">
		<xsd:sequence>
			<xsd:element name="name" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Data Analysis  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DataAnalysisType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="dataAnalysisMethod"
				type="DataAnalysisMethodType"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Data Analysis Method :  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DataAnalysisMethodType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="samplePreparation"
				type="xsd:string"/>
			<xsd:choice>
				<xsd:element name="arrheniusFit" type="ArrheniusFitType"/>
				<xsd:element name="otherEquation" type="xsd:string"/>
			</xsd:choice>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Data Analysis Method :  Intrinsic Diffusion Data Analysis Type-->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="IntrinsicDataAnalysisMethodType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="samplePreparation"
				type="xsd:string"/>
			<xsd:choice>
				<xsd:element minOccurs="0" name="thermodynamicFactor" type="xsd:string"/>
				<xsd:element name="arrheniusFit" type="ArrheniusFitType"/>
				<xsd:element minOccurs="0" name="otherEquation" type="xsd:string"/>
			</xsd:choice>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Data Analysis Method Type : Arrhenius Fit  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ArrheniusFitType">
		<xsd:annotation>
			<xsd:documentation>
				<div class="summary">Arrhenius Fit (D=D0*exp(-Q/RT)</div>
				<div class="description">
					<p>The dependence of the rate constant k of chemical reactions on the temperature T (in absolute temperature kelvin) and where 
            -Q is the pre-exponential factor or simply the prefactor and R is the Universal gas constant.</p>
				</div>
			</xsd:documentation>
		</xsd:annotation>
		<xsd:sequence maxOccurs="unbounded" minOccurs="0">
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="phase" type="Phase-Magnetic"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="temperature"
				type="TemperatureType"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="d0" type="d0Type"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="q" type="qType"/>
			<xsd:element name="description" type="xsd:string" maxOccurs="unbounded" minOccurs="0"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Phase - Magnetic  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Datum  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Datum">
		<xsd:sequence>
			<xsd:element name="id" type="xsd:integer"/>
			<xsd:element name="type" type="xsd:string"/>
			<xsd:element name="description" type="xsd:string"/>
			<xsd:element name="properties" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="comment" type="xsd:string"/>
			<xsd:element name="measuredParameters" type="MaterialProperty"/>
			<xsd:element maxOccurs="unbounded" name="value" type="Quantity"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Derived Value  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DerivedValueType">
		<xsd:sequence>
			<xsd:element maxOccurs="1" minOccurs="0" name="equation" type="xsd:string"/>
			<xsd:element name="value" type="Quantity"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Diffusing Species  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DiffusingSpecies">
		<xsd:sequence>
			<xsd:element name="element" type="ChemicalElement"/>
			<xsd:element minOccurs="0" name="materialPurity" type="xsd:double"/>
			<xsd:element name="isotope" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Diffusivity Experiment  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DiffusivityExperiment">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" name="experimentType" type="ExperimentType"/>
			<xsd:element maxOccurs="unbounded" name="data" type="Datum"/>
			<xsd:element maxOccurs="unbounded" minOccurs="2" name="materials" type="Materials"/>
			<xsd:element name="id" type="xsd:integer"/>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="table" type="Table"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Environmental Condition  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="EnvironmentalConditionType">
		<xsd:sequence> </xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Experiment  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Experiment">
		<xsd:sequence>
			<xsd:element name="experimentalDetails" type="Interdiffusion"/>
			<xsd:element name="id" type="xsd:integer" minOccurs="0"/>
			<xsd:element name="citation" type="CitationType"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Experimental Conditions  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ExperimentalConditionsType">
		<xsd:sequence>
			<xsd:element maxOccurs="1" minOccurs="1" name="time" type="TimeType"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="temperature" type="TemperatureType"/>
			<xsd:element name="environment" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  ExperimentType  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ExperimentType">
		<xsd:sequence> </xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Experiment Type: Tracer Diffusivity Experiment  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Interdiffusion">
		<xsd:sequence>
			<xsd:element name="material" type="Material" maxOccurs="1" minOccurs="1"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="experimentalConditions"
				type="ExperimentalConditionsType"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="measurementSpec" type="xsd:string"/>
			<xsd:element name="measurementDescription" type="xsd:string"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="measuredValues" type="MeasuredValuesType"
			/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  FormOfMatter  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="FormOfMatter">
		<xsd:choice>
			<xsd:element name="singleCrystalline" type="SingleCrystallineType"/>
			<xsd:element minOccurs="0" name="polycrystalline" type="PolyCrystallineType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  FormOfMatter:Polycrystalline -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="PolyCrystallineType">
		<xsd:sequence minOccurs="0">
			<xsd:choice minOccurs="0">
				<xsd:element name="averageGrainSize" type="AverageGrainSize" maxOccurs="1"
					minOccurs="0"/>
				<xsd:element name="GrainSizeRange" type="Range" maxOccurs="1" minOccurs="0"/>
			</xsd:choice>
			<xsd:sequence minOccurs="0">
				<xsd:element minOccurs="0" name="lengthunits" type="LengthUnitType"/>
			</xsd:sequence>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Average Grain Size  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="AverageGrainSize">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="averageGrainSize" type="xsd:double"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  FormOfMatter: Single Crystalline  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SingleCrystallineType"/>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Image  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ImageType">
		<xsd:sequence>
			<xsd:element name="FileType" type="xsd:string"/>
			<xsd:element name="Digitalidentifier" type="xsd:anyURI"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Material  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Material Compound -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MaterialCompound">
		<xsd:sequence>
			<xsd:element name="materialName" type="xsd:string"/>
			<xsd:element name="phase" type="Phase"/>
			<xsd:element name="molecularFormula" type="MolecularFormula"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  MaterialProperty  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MaterialProperty">
		<xsd:sequence>
			<xsd:element name="name" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Materials  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Materials">
		<xsd:sequence maxOccurs="unbounded" minOccurs="0">
			<xsd:element maxOccurs="unbounded" name="Material" type="Material" minOccurs="1"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measured Value  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MeasuredValueType">
		<xsd:sequence>
			<xsd:choice> </xsd:choice>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measured Values  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MeasuredValuesType">
		<xsd:sequence maxOccurs="unbounded">
			<xsd:element name="quantity" type="xsd:string"/>
			<xsd:element name="value" type="xsd:float"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Condition  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MeasurementConditionType">
		<xsd:sequence> </xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Material">
		<xsd:sequence maxOccurs="unbounded" minOccurs="1">
			<xsd:element name="MaterialName" type="xsd:string"/>
			<xsd:element name="CrystalStructure" type="xsd:string"/>
			<xsd:element minOccurs="0" name="MaterialPurity-percent" type="xsd:string"/>
			<xsd:element minOccurs="0" name="SpaceGroup" type="xsd:string"/>
			<xsd:element name="Composition" type="Composition" maxOccurs="unbounded" minOccurs="0"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="materialForm" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="MeasurementType">
		<xsd:sequence>
			<xsd:element name="type" type="xsd:string"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="experimentalMethod"
				type="ExperimentalMethodType"/>
			<xsd:element name="dataCollectionMethod" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Direct Method  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="DirectMethodType">
		<xsd:choice>
			<xsd:element name="EPMA" type="ElectronProbeMicroAnalysisType"/>
			<xsd:element name="SIMS" type="SecondaryIonMassSpectroscopyType"/>
			<xsd:element name="RBS" type="RutherfordBackscatteringMethodsType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Direct Method: EPMA  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ElectronProbeMicroAnalysisType">
		<xsd:choice>
			<xsd:element name="EPMAInstrumentBrand" type="xsd:string"/>
			<xsd:element name="beamEnergy" type="xsd:double"/>
			<xsd:element name="beamEnergyUnit" type="EnergyUnitType"/>
			<xsd:element name="probeSize" type="xsd:double"/>
			<xsd:element name="probeSizeUnit" type="LengthUnitType"/>
			<xsd:element name="correctionMethod" type="xsd:string"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Direct Method: RBS  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="RutherfordBackscatteringMethodsType">
		<xsd:sequence>
			<xsd:element name="RBSInstrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Direct Method: SIMS  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SecondaryIonMassSpectroscopyType">
		<xsd:sequence>
			<xsd:element name="simsInstrument" type="xsd:string"/>
			<xsd:element name="primaryBeamSource" type="xsd:string"/>
			<xsd:element name="energy" type="xsd:double"/>
			<xsd:element name="energyUnit" type="EnergyUnitType"/>
			<xsd:element name="rasterArea" type="xsd:double"/>
			<xsd:element name="rasterAreaUnit" type="LengthUnitType"/>
			<xsd:element name="detectionArea" type="xsd:double"/>
			<xsd:element name="detectionAreaUnit" type="LengthUnitType"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Indirect Method  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="IndirectMethodType">
		<xsd:choice>
			<xsd:element name="nuclearMethods" type="NuclearMethodsType"/>
			<xsd:element name="mechanicalSpectroscopy" type="MechanicalSpectroscopyType"/>
			<xsd:element name="electricalMethods" type="ElectricalMethodsType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Indirect Method: Nuclear Methods  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="NuclearMethodsType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Indirect Method: Mechanical Spectroscopy  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MechanicalSpectroscopyType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Indirect Method: Electrical Methods  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ElectricalMethodsType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Methods  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="RadiotracerType">
		<xsd:choice>
			<xsd:element name="serialSectioning" type="SerialSectioningType"/>
			<xsd:element name="gruzinMethod" type="ResidualActivityMethodType"/>
			<xsd:element name="surfaceActivityDecreaseMethod"
				type="SurfaceActivityDecreaseMethodType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Method: Serial Sectioning Methods  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SerialSectioningType">
		<xsd:choice>
			<xsd:element name="macroSectioning" type="MacroSectioningType"/>
			<xsd:element name="microSectioning" type="MicroSectioningType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Method: Serial Sectioning Methods : Macro-Sectioning  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MacroSectioningType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Method: Serial Sectioning Methods : Micro-Sectioning  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MicroSectioningType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Method: Residual Activity Method  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ResidualActivityMethodType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type: Radiotracer Method: Surface Activity Decrease Method  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SurfaceActivityDecreaseMethodType">
		<xsd:sequence>
			<xsd:element name="instrument" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Measurement Type Method  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ExperimentalMethodType">
		<xsd:choice>
			<xsd:element maxOccurs="1" minOccurs="1" name="direct" type="DirectMethodType"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="indirect" type="IndirectMethodType"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Molecular Formula  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MolecularFormula">
		<xsd:choice>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="element"
				type="ConstituentElement"/>
		</xsd:choice>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Phase  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Phases  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Phase">
		<xsd:sequence>
			<xsd:element name="name" type="xsd:string"/>
			<xsd:element name="crystalStructure" type="CrystalStructure"/>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="Phases">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="temperature" type="Quantity"/>
			<xsd:element maxOccurs="unbounded" name="phase" type="Phase"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Procedures  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="ProcedureType">
		<xsd:sequence>
			<xsd:element maxOccurs="1" minOccurs="1" name="procedureName" type="xsd:string"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="procedureDescription" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Point  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Point">
		<xsd:sequence>
			<xsd:element name="sampleID" type="xsd:string"/>
			<xsd:element name="x" type="xsd:double"/>
			<xsd:element name="y" type="xsd:double"/>
			<xsd:element name="xUnit" type="UnitOfMeasure"/>
			<xsd:element name="yUnit" type="UnitOfMeasure"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Profile  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Profile">
		<xsd:sequence> </xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Profile:Gradient  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Gradient">
		<xsd:sequence>
			<xsd:element name="name" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="value" type="Quantity"/>
			<xsd:element name="unit" type="UnitOfMeasure"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Profile:Series  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Series">
		<xsd:sequence>
			<xsd:element name="xLabel" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="value" type="Quantity"/>
			<xsd:element name="xUnit" type="UnitOfMeasure"/>
			<xsd:element name="yLabel" type="xsd:string"/>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="value" type="Quantity"/>
			<xsd:element name="yUnit" type="UnitOfMeasure"/>
			<xsd:element name="numberOfDataPoints" type="xsd:integer"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Quantity  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Quantity">
		<xsd:sequence>
			<xsd:element name="sampleID" type="xsd:string"/>
			<xsd:element name="value" type="xsd:double"/>
			<xsd:element minOccurs="0" name="uncertainty" type="Uncertainty"/>
			<xsd:element name="unit" type="UnitOfMeasure"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Sample Preparation Type -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SamplePreparationType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" name="sampleGeometry" type="SampleGeometryType"/>
			<xsd:element maxOccurs="unbounded" name="samplePreparationProcedure"
				type="ProcedureType"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Sample Geometry -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="SampleGeometryType">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="1" name="geometry"
				type="MaterialGeometryType"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Material Geometry -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="MaterialGeometryType">
		<xsd:sequence>
			<xsd:element name="MaterialName" type="xsd:string"/>
			<xsd:element name="geometry" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Table -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="qType">
		<xsd:sequence>
			<xsd:element name="q" type="xsd:double"/>
			<xsd:element name="qUnit" type="UnitOfMeasure"/>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="Table">
		<xsd:sequence>
			<xsd:element name="headers" type="Headers"/>
			<xsd:element name="rows" type="Rows"/>
		</xsd:sequence>
		<xsd:attribute name="name" type="xsd:string" use="optional"/>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Headers -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Headers">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" name="column" type="Column"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Rows -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Rows">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" name="row" type="Row"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Row -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Row">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" name="column" type="Column"/>
		</xsd:sequence>
		<xsd:attribute name="id" type="xsd:string" use="required"/>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Column -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Column">
		<xsd:simpleContent>
			<xsd:extension base="xsd:string">
				<xsd:attribute name="id" type="xsd:string" use="required"/>
			</xsd:extension>
		</xsd:simpleContent>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Temperature  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="TemperatureType">
		<xsd:sequence>
			<xsd:element name="value" type="xsd:float"/>
			<xsd:element name="unit" type="xsd:string"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Time  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="TimeType">
		<xsd:sequence>
			<xsd:element name="value" type="xsd:float"/>
			<xsd:element name="unit" type="xsd:string"/>
			<xsd:element minOccurs="0" name="uncertainty" type="Uncertainty"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!-- Range  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Range">
		<xsd:sequence>
			<xsd:element name="min" type="xsd:double"/>
			<xsd:element name="max" type="xsd:double"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Uncertainty  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:complexType name="Uncertainty">
		<xsd:sequence>
			<xsd:element name="type">
				<xsd:simpleType>
					<xsd:restriction base="xsd:string">
						<xsd:enumeration value="amount"/>
						<xsd:enumeration value="fraction"/>
					</xsd:restriction>
				</xsd:simpleType>
			</xsd:element>
			<xsd:element name="value" type="xsd:double"/>
		</xsd:sequence>
	</xsd:complexType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Chemical Constituent Quantity Unit  TODO Integrate UnitsML -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="ConstituentQuantityUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="mass fraction"/>
			<xsd:enumeration value="mass percent"/>
			<xsd:enumeration value="mole fraction"/>
			<xsd:enumeration value="mole percent"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Energy Unit  TODO Integrate UnitsML -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="EnergyUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="megavolts"/>
			<xsd:enumeration value="kilovolts"/>
			<xsd:enumeration value="volts"/>
			<xsd:enumeration value="millivolts"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Length Unit  TODO Integrate UnitsML -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="LengthUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="millimeter"/>
			<xsd:enumeration value="micrometer"/>
			<xsd:enumeration value="picometer"/>
			<xsd:enumeration value="meter"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Temperature Unit  TODO Integrate UnitsML -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="TemperatureUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="Kelvin"/>
			<xsd:enumeration value="Celsius"/>
			<xsd:enumeration value="Fahrenheit"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Time Unit TODO Integrate UnitsML  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="TimeUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="years"/>
			<xsd:enumeration value="days"/>
			<xsd:enumeration value="hours"/>
			<xsd:enumeration value="minutes"/>
			<xsd:enumeration value="seconds"/>
			<xsd:enumeration value="milliseconds"/>
			<xsd:enumeration value="microseconds"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  Unit: Velocity Unit TODO Integrate UnitsML  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="VelocityUnitType">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="m/s"/>
			<xsd:enumeration value="mm/s"/>
		</xsd:restriction>
	</xsd:simpleType>
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<!--  UnitOfMeasure  -->
	<!-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
	<xsd:simpleType name="UnitOfMeasure">
		<xsd:restriction base="xsd:string"/>
	</xsd:simpleType>
	<xsd:simpleType name="Phase-Magnetic">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="Ferromagnetic"/>
			<xsd:enumeration value="Paramagnetic"/>
		</xsd:restriction>
	</xsd:simpleType>
	<xsd:complexType name="d0Type">
		<xsd:sequence>
			<xsd:element name="d0" type="xsd:double"/>
			<xsd:element name="d0Unit" type="UnitOfMeasure"/>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="Composition">
		<xsd:sequence maxOccurs="1" minOccurs="1">
			<xsd:element maxOccurs="1" minOccurs="1" name="element" type="ChemicalElement"/>
			<xsd:element maxOccurs="1" minOccurs="1" name="CompositionRange" type="Range"/>
			<xsd:element name="quantityUnit" type="ConstituentQuantityUnitType"/>
		</xsd:sequence>
	</xsd:complexType>
</xsd:schema>

```

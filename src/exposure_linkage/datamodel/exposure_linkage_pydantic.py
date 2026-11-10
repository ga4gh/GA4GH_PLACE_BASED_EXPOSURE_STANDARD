from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'expo',
     'default_range': 'string',
     'description': 'Describes how an environmental exposure dataset was linked to '
                    'cohort participants. One ExposureLinkageRecord = one exposure '
                    'variable linked in one cohort. Converted from "Implementation '
                    '1 - GA4GH Metadata Schema".',
     'id': 'https://w3id.org/ga4gh/exposure-linkage',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'exposure_linkage',
     'prefixes': {'CAS': {'prefix_prefix': 'CAS',
                          'prefix_reference': 'https://identifiers.org/cas:'},
                  'DTXSID': {'prefix_prefix': 'DTXSID',
                             'prefix_reference': 'https://comptox.epa.gov/dashboard/chemical/details/'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'ExO': {'prefix_prefix': 'ExO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/ExO_'},
                  'INCHIKEY': {'prefix_prefix': 'INCHIKEY',
                               'prefix_reference': 'https://identifiers.org/inchikey:'},
                  'MESH': {'prefix_prefix': 'MESH',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'ORCID': {'prefix_prefix': 'ORCID',
                            'prefix_reference': 'https://orcid.org/'},
                  'PUBCHEM': {'prefix_prefix': 'PUBCHEM',
                              'prefix_reference': 'http://rdf.ncbi.nlm.nih.gov/pubchem/compound/CID'},
                  'expo': {'prefix_prefix': 'expo',
                           'prefix_reference': 'https://w3id.org/ga4gh/exposure-linkage/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': 'src/exposure_linkage/schema/exposure_linkage.yaml',
     'title': 'GA4GH Environmental Exposure Linkage Metadata',
     'types': {'CURIE': {'base': 'URIorCURIE',
                         'description': 'Compact identifier, e.g. INCHIKEY:..., '
                                        'ENVO:..., MESH:...',
                         'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                         'name': 'CURIE',
                         'typeof': 'uriorcurie',
                         'uri': 'xsd:anyURI'},
               'PartialDate': {'base': 'str',
                               'description': 'ISO 8601 YYYY, YYYY-MM or '
                                              'YYYY-MM-DD.',
                               'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                               'name': 'PartialDate',
                               'pattern': '^\\d{4}(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\\d|3[01]))?)?$',
                               'typeof': 'string',
                               'uri': 'xsd:string'},
               'RegionCode': {'base': 'str',
                              'description': 'ISO 3166-1 alpha-2 or ISO 3166-2 '
                                             'subdivision (e.g. US-NC).',
                              'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                              'name': 'RegionCode',
                              'pattern': '^(AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|YE|YT|ZA|ZM|ZW)(-[A-Z0-9]{1,3})?$',
                              'typeof': 'string',
                              'uri': 'xsd:string'},
               'UcumCode': {'base': 'str',
                            'description': 'UCUM case-sensitive code, e.g. ug/m3, '
                                           'ng/m3, [ppb], [ppm], Cel, mm, m/s, '
                                           'W/m2, /km2, %, 1 (dimensionless '
                                           'index). dB(A) has no UCUM code - use '
                                           '"dB" with weighting recorded in '
                                           'exposure_variable.',
                            'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                            'name': 'UcumCode',
                            'typeof': 'string',
                            'uri': 'xsd:string'}}} )

class CountryCodeEnum(str, Enum):
    """
    ISO 3166-1 alpha-2, officially assigned codes (GB, not UK).
    """
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class ExposureDomainEnum(str, Enum):
    AIR_POLLUTION = "AIR_POLLUTION"
    CLIMATE_WEATHER = "CLIMATE_WEATHER"
    GREEN_SPACE = "GREEN_SPACE"
    BLUE_SPACE = "BLUE_SPACE"
    NOISE = "NOISE"
    SOCIODEMOGRAPHIC = "SOCIODEMOGRAPHIC"
    BUILT_ENVIRONMENT = "BUILT_ENVIRONMENT"
    WATER_QUALITY = "WATER_QUALITY"
    LIGHT_POLLUTION = "LIGHT_POLLUTION"
    BIODIVERSITY = "BIODIVERSITY"
    INDOOR_HOME_ENVIRONMENT = "INDOOR_HOME_ENVIRONMENT"
    OTHER = "OTHER"


class DataOriginEnum(str, Enum):
    MONITORING_STATION = "MONITORING_STATION"
    LAND_USE_REGRESSION = "LAND_USE_REGRESSION"
    CHEMICAL_TRANSPORT_MODEL = "CHEMICAL_TRANSPORT_MODEL"
    SATELLITE_DERIVED = "SATELLITE_DERIVED"
    PERSONAL_MONITOR = "PERSONAL_MONITOR"
    QUESTIONNAIRE = "QUESTIONNAIRE"
    ADMINISTRATIVE_RECORD = "ADMINISTRATIVE_RECORD"
    REANALYSIS = "REANALYSIS"
    """
    Added - ERA5-type products were otherwise unclassifiable.
    """
    OTHER = "OTHER"


class GeographicScopeEnum(str, Enum):
    COUNTRIES_OR_REGIONS = "COUNTRIES_OR_REGIONS"
    EU27 = "EU27"
    GLOBAL = "GLOBAL"


class SpatialResolutionTypeEnum(str, Enum):
    GRID_METRIC = "GRID_METRIC"
    GRID_DEGREE = "GRID_DEGREE"
    ADMINISTRATIVE_UNIT = "ADMINISTRATIVE_UNIT"
    POINT_ADDRESS = "POINT_ADDRESS"
    POINT_GPS = "POINT_GPS"


class TemporalResolutionEnum(str, Enum):
    SUB_HOURLY = "SUB_HOURLY"
    HOURLY = "HOURLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    SEASONAL = "SEASONAL"
    ANNUAL = "ANNUAL"
    MULTI_YEAR_AVERAGE = "MULTI_YEAR_AVERAGE"
    EVENT_BASED = "EVENT_BASED"
    STATIC = "STATIC"
    PERIODIC_UPDATE = "PERIODIC_UPDATE"


class ValidationMetricEnum(str, Enum):
    R2 = "R2"
    RMSE = "RMSE"
    NRMSE_PCT = "NRMSE_PCT"
    MEAN_BIAS = "MEAN_BIAS"
    RELATIVE_BIAS_PCT = "RELATIVE_BIAS_PCT"
    PEARSON_R = "PEARSON_R"


class ValidationDesignEnum(str, Enum):
    LOOCV_SPATIAL = "LOOCV_SPATIAL"
    INDEPENDENT_TEST_SET_SPATIAL = "INDEPENDENT_TEST_SET_SPATIAL"
    TEMPORAL = "TEMPORAL"
    OVERALL = "OVERALL"
    GROUND_MONITOR_COMPARISON = "GROUND_MONITOR_COMPARISON"


class UncertaintyTypeEnum(str, Enum):
    NOT_AVAILABLE = "NOT_AVAILABLE"
    SD_PER_UNIT = "SD_PER_UNIT"
    PREDICTION_INTERVAL_95 = "PREDICTION_INTERVAL_95"
    FULL_PREDICTIVE_DISTRIBUTION = "FULL_PREDICTIVE_DISTRIBUTION"
    MODEL_LEVEL_RMSE_ONLY = "MODEL_LEVEL_RMSE_ONLY"


class SpatialLinkageUnitEnum(str, Enum):
    GEOCODED_ADDRESS = "GEOCODED_ADDRESS"
    GPS_COORDINATE = "GPS_COORDINATE"
    POSTCODE_CENTROID = "POSTCODE_CENTROID"
    CENSUS_TRACT_CENTROID = "CENSUS_TRACT_CENTROID"
    LSOA_CENTROID = "LSOA_CENTROID"
    MUNICIPALITY_CENTROID = "MUNICIPALITY_CENTROID"
    OTHER_AREAL_CENTROID = "OTHER_AREAL_CENTROID"
    GRID_CELL_CONTAINING_ADDRESS = "GRID_CELL_CONTAINING_ADDRESS"


class CentroidWeightingEnum(str, Enum):
    GEOMETRIC = "GEOMETRIC"
    POPULATION_WEIGHTED = "POPULATION_WEIGHTED"
    AREA_WEIGHTED = "AREA_WEIGHTED"


class LinkageOperationEnum(str, Enum):
    POINT_IN_POLYGON = "POINT_IN_POLYGON"
    CIRCULAR_BUFFER = "CIRCULAR_BUFFER"
    NETWORK_BUFFER = "NETWORK_BUFFER"
    NEAREST_FEATURE = "NEAREST_FEATURE"
    AREAL_INTERPOLATION = "AREAL_INTERPOLATION"
    INTERSECTION = "INTERSECTION"
    KERNEL_DENSITY_WEIGHTED = "KERNEL_DENSITY_WEIGHTED"
    ADMINISTRATIVE_ASSIGNMENT = "ADMINISTRATIVE_ASSIGNMENT"


class NetworkModeEnum(str, Enum):
    WALKING = "WALKING"
    CYCLING = "CYCLING"
    DRIVING = "DRIVING"
    PUBLIC_TRANSPORT = "PUBLIC_TRANSPORT"


class GeocodingPrecisionEnum(str, Enum):
    BUILDING = "BUILDING"
    """
    < 5 m
    """
    PARCEL = "PARCEL"
    """
    < 10 m
    """
    STREET = "STREET"
    """
    < 50 m
    """
    POSTCODE_CENTROID = "POSTCODE_CENTROID"
    """
    < 500 m
    """
    CENSUS_UNIT_CENTROID = "CENSUS_UNIT_CENTROID"
    """
    > 500 m
    """
    MIXED = "MIXED"
    UNKNOWN = "UNKNOWN"


class AggregationEnum(str, Enum):
    ANNUAL_MEAN = "ANNUAL_MEAN"
    MONTHLY_MEAN = "MONTHLY_MEAN"
    DAILY_MEAN = "DAILY_MEAN"
    DAILY_MAX = "DAILY_MAX"
    DAILY_MIN = "DAILY_MIN"
    EIGHT_HOUR_MEAN = "EIGHT_HOUR_MEAN"
    WARM_SEASON_MEAN = "WARM_SEASON_MEAN"
    COLD_SEASON_MEAN = "COLD_SEASON_MEAN"
    NIGHT_TIME_MEAN = "NIGHT_TIME_MEAN"
    MULTI_YEAR_MEAN = "MULTI_YEAR_MEAN"
    CUMULATIVE_SUM = "CUMULATIVE_SUM"
    PERCENTILE = "PERCENTILE"
    PRESENCE_ABSENCE = "PRESENCE_ABSENCE"
    DISTANCE_TO_NEAREST = "DISTANCE_TO_NEAREST"
    COUNT_WITHIN_BUFFER = "COUNT_WITHIN_BUFFER"
    MEAN_WITHIN_BUFFER = "MEAN_WITHIN_BUFFER"
    """
    Buffer geometry lives in linkage.operation - not duplicated here.
    """
    COMPOSITE_INDEX = "COMPOSITE_INDEX"
    RAW_TIME_SERIES = "RAW_TIME_SERIES"


class CoverageUnitEnum(str, Enum):
    PARTICIPANTS = "PARTICIPANTS"
    HOUSEHOLDS = "HOUSEHOLDS"
    CLINICAL_SITES = "CLINICAL_SITES"
    HOSPITALS = "HOSPITALS"
    GEOGRAPHIC_UNITS = "GEOGRAPHIC_UNITS"


class ExposureWindowEnum(str, Enum):
    YEAR_BEFORE_RECRUITMENT = "YEAR_BEFORE_RECRUITMENT"
    N_YEARS_BEFORE_INDEX = "N_YEARS_BEFORE_INDEX"
    PRENATAL = "PRENATAL"
    PERICONCEPTION = "PERICONCEPTION"
    INFANCY = "INFANCY"
    EARLY_CHILDHOOD = "EARLY_CHILDHOOD"
    ADOLESCENCE = "ADOLESCENCE"
    LIFETIME_CUMULATIVE = "LIFETIME_CUMULATIVE"
    TIME_VARYING_ANNUAL = "TIME_VARYING_ANNUAL"
    CRITICAL_WINDOW = "CRITICAL_WINDOW"


class ResidentialHistoryEnum(str, Enum):
    BASELINE_ONLY = "BASELINE_ONLY"
    FULL_HISTORY = "FULL_HISTORY"
    PARTIAL_HISTORY = "PARTIAL_HISTORY"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"



class ExposureLinkageCollection(ConfiguredBaseModel):
    """
    Container so one file can hold many records.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage', 'tree_root': True})

    records: list[ExposureLinkageRecord] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageCollection']} })


class ExposureLinkageRecord(ConfiguredBaseModel):
    """
    One exposure variable linked to one cohort.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    id: str = Field(default=..., description="""Stable record identifier, e.g. UKB-NO2-ELAPSE-2010.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    cohort: Cohort = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    exposure: ExposureVariable = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    source_data: SourceDataset = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    linkage: Linkage = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    creators: Optional[list[Person]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord'], 'recommended': True} })


class Cohort(ConfiguredBaseModel):
    """
    CSV: Cohort / Study Name; Country of Participant Data Collection
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    name: str = Field(default=..., description="""Full name, e.g. UK Biobank.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    acronym: str = Field(default=..., description="""e.g. UKB. Split out of the old \"Name (ACRONYM)\" string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    collection_countries: list[CountryCodeEnum] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })


class ExposureVariable(ConfiguredBaseModel):
    """
    CSV: Exposure Domain; Exposure Variable Name; Ontology Term ID; Unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'OTHER domain must be specified.',
                    'postconditions': {'slot_conditions': {'domain_other': {'name': 'domain_other',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'domain': {'equals_string': 'OTHER',
                                                                     'name': 'domain'}}}}]})

    domain: ExposureDomainEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })
    domain_other: Optional[str] = Field(default=None, description="""Required when domain = OTHER.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })
    name: str = Field(default=..., description="""Descriptive term, e.g. NO2, PM2.5, Lden, NDVI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    ontology_terms: Optional[list[URIorCURIE]] = Field(default=None, description="""Chemicals: INCHIKEY (preferred), PUBCHEM, DTXSID, CAS. Physical/environmental: ExO, ENVO, MESH. Leave empty if none exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable'], 'recommended': True} })
    unit: Optional[str] = Field(default=None, description="""Omit for categorical variables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })
    is_categorical: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })


class SourceDataset(ConfiguredBaseModel):
    """
    The upstream exposure product (model, satellite, monitors...).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Periodic update needs a frequency.',
                    'postconditions': {'slot_conditions': {'update_frequency': {'name': 'update_frequency',
                                                                                'required': True}}},
                    'preconditions': {'slot_conditions': {'temporal_resolution': {'equals_string': 'PERIODIC_UPDATE',
                                                                                  'name': 'temporal_resolution'}}}}]})

    origin: DataOriginEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    dataset_name: str = Field(default=..., description="""e.g. ELAPSE LUR, ERA5, MODIS MOD13A3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    dataset_version: str = Field(default=..., description="""Version number or release year, e.g. 2.0, 006, 2023.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    citations: list[Citation] = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    geographic_coverage: GeographicCoverage = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    spatial_resolution: SpatialResolution = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    temporal_coverage: TemporalCoverage = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    temporal_resolution: TemporalResolutionEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    update_frequency: Optional[str] = Field(default=None, description="""For PERIODIC_UPDATE, e.g. P5Y (ISO 8601 duration).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    validation_metrics: Optional[list[ValidationMetric]] = Field(default=None, description="""Empty list + validation_reported=false means not validated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset'], 'recommended': True} })
    validation_reported: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    uncertainty: Optional[Uncertainty] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset'], 'recommended': True} })

    @field_validator('update_frequency')
    def pattern_update_frequency(cls, v):
        pattern=re.compile(r"^P(\d+Y)?(\d+M)?(\d+W)?(\d+D)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid update_frequency format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid update_frequency format: {v}"
            raise ValueError(err_msg)
        return v


class Citation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'doi': {'name': 'doi', 'required': True}}},
                    {'slot_conditions': {'url': {'name': 'url', 'required': True}}},
                    {'slot_conditions': {'text': {'name': 'text', 'required': True}}}],
         'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    doi: Optional[str] = Field(default=None, description="""Bare DOI, without the doi: prefix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    url: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    accessed: Optional[date] = Field(default=None, description="""Required when url is given without a DOI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    text: Optional[str] = Field(default=None, description="""Free-text citation if no DOI/URL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    used_for_linkage: Optional[bool] = Field(default=None, description="""Replaces the old \"*\" marker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })

    @field_validator('doi')
    def pattern_doi(cls, v):
        pattern=re.compile(r"^10\.\d{4,9}/\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid doi format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid doi format: {v}"
            raise ValueError(err_msg)
        return v


class GeographicCoverage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Country/region scope needs region codes.',
                    'postconditions': {'slot_conditions': {'regions': {'name': 'regions',
                                                                       'required': True}}},
                    'preconditions': {'slot_conditions': {'scope': {'equals_string': 'COUNTRIES_OR_REGIONS',
                                                                    'name': 'scope'}}}}]})

    scope: GeographicScopeEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })
    regions: Optional[list[str]] = Field(default=None, description="""Required when scope = COUNTRIES_OR_REGIONS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })
    description: Optional[str] = Field(default=None, description="""Optional note, e.g. \"UK-wide\", \"multiple provinces\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })


class SpatialResolution(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Metric grid needs cell size.',
                    'postconditions': {'slot_conditions': {'cell_height': {'name': 'cell_height',
                                                                           'required': True},
                                                           'cell_width': {'name': 'cell_width',
                                                                          'required': True}}},
                    'preconditions': {'slot_conditions': {'type': {'equals_string': 'GRID_METRIC',
                                                                   'name': 'type'}}}},
                   {'description': 'Degree grid needs cell size.',
                    'postconditions': {'slot_conditions': {'cell_height': {'name': 'cell_height',
                                                                           'required': True},
                                                           'cell_width': {'name': 'cell_width',
                                                                          'required': True}}},
                    'preconditions': {'slot_conditions': {'type': {'equals_string': 'GRID_DEGREE',
                                                                   'name': 'type'}}}},
                   {'description': 'Admin unit needs a unit name.',
                    'postconditions': {'slot_conditions': {'admin_unit_name': {'name': 'admin_unit_name',
                                                                               'required': True}}},
                    'preconditions': {'slot_conditions': {'type': {'equals_string': 'ADMINISTRATIVE_UNIT',
                                                                   'name': 'type'}}}}]})

    type: SpatialResolutionTypeEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution', 'Uncertainty']} })
    cell_width: Optional[float] = Field(default=None, description="""For GRID_METRIC (metres) or GRID_DEGREE (degrees).""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    cell_height: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    admin_unit_name: Optional[str] = Field(default=None, description="""For ADMINISTRATIVE_UNIT, e.g. LSOA, census tract.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    admin_unit_approx_population: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })


class TemporalCoverage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Ongoing datasets need a last-updated date.',
                    'postconditions': {'slot_conditions': {'last_updated': {'name': 'last_updated',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'ongoing': {'equals_string': 'true',
                                                                      'name': 'ongoing'}}}}]})

    start: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    end: Optional[str] = Field(default=None, description="""Omit when ongoing = true.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    ongoing: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    last_updated: Optional[str] = Field(default=None, description="""Required when ongoing = true.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })


class ValidationMetric(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    metric: ValidationMetricEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric']} })
    validation_design: Optional[ValidationDesignEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric']} })
    value: float = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric', 'Uncertainty']} })
    unit: Optional[str] = Field(default=None, description="""For RMSE / mean bias; omit for R2, r, %.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })


class Uncertainty(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    type: UncertaintyTypeEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution', 'Uncertainty']} })
    value: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric', 'Uncertainty']} })
    lower: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })
    upper: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })
    unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })
    carried_to_participant_level: Optional[bool] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })


class Linkage(ConfiguredBaseModel):
    """
    How exposure values were assigned to participants.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Circular buffer needs a radius.',
                    'postconditions': {'slot_conditions': {'buffer_radii_m': {'name': 'buffer_radii_m',
                                                                              'required': True}}},
                    'preconditions': {'slot_conditions': {'operation': {'equals_string': 'CIRCULAR_BUFFER',
                                                                        'name': 'operation'}}}},
                   {'description': 'Network buffer needs a mode.',
                    'postconditions': {'slot_conditions': {'network_mode': {'name': 'network_mode',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'operation': {'equals_string': 'NETWORK_BUFFER',
                                                                        'name': 'operation'}}}},
                   {'description': 'Kernel density needs bandwidth.',
                    'postconditions': {'slot_conditions': {'kernel_bandwidth_m': {'name': 'kernel_bandwidth_m',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'operation': {'equals_string': 'KERNEL_DENSITY_WEIGHTED',
                                                                        'name': 'operation'}}}},
                   {'description': 'Multi-year mean needs N.',
                    'postconditions': {'slot_conditions': {'aggregation_n': {'name': 'aggregation_n',
                                                                             'required': True}}},
                    'preconditions': {'slot_conditions': {'aggregation': {'equals_string': 'MULTI_YEAR_MEAN',
                                                                          'name': 'aggregation'}}}},
                   {'description': 'Percentile needs N.',
                    'postconditions': {'slot_conditions': {'aggregation_n': {'name': 'aggregation_n',
                                                                             'required': True}}},
                    'preconditions': {'slot_conditions': {'aggregation': {'equals_string': 'PERCENTILE',
                                                                          'name': 'aggregation'}}}},
                   {'description': 'POSTCODE_CENTROID needs centroid weighting.',
                    'postconditions': {'slot_conditions': {'centroid_weighting': {'name': 'centroid_weighting',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'spatial_linkage_unit': {'equals_string': 'POSTCODE_CENTROID',
                                                                                   'name': 'spatial_linkage_unit'}}}},
                   {'description': 'CENSUS_TRACT_CENTROID needs centroid weighting.',
                    'postconditions': {'slot_conditions': {'centroid_weighting': {'name': 'centroid_weighting',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'spatial_linkage_unit': {'equals_string': 'CENSUS_TRACT_CENTROID',
                                                                                   'name': 'spatial_linkage_unit'}}}},
                   {'description': 'LSOA_CENTROID needs centroid weighting.',
                    'postconditions': {'slot_conditions': {'centroid_weighting': {'name': 'centroid_weighting',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'spatial_linkage_unit': {'equals_string': 'LSOA_CENTROID',
                                                                                   'name': 'spatial_linkage_unit'}}}},
                   {'description': 'MUNICIPALITY_CENTROID needs centroid weighting.',
                    'postconditions': {'slot_conditions': {'centroid_weighting': {'name': 'centroid_weighting',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'spatial_linkage_unit': {'equals_string': 'MUNICIPALITY_CENTROID',
                                                                                   'name': 'spatial_linkage_unit'}}}},
                   {'description': 'OTHER_AREAL_CENTROID needs centroid weighting.',
                    'postconditions': {'slot_conditions': {'centroid_weighting': {'name': 'centroid_weighting',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'spatial_linkage_unit': {'equals_string': 'OTHER_AREAL_CENTROID',
                                                                                   'name': 'spatial_linkage_unit'}}}},
                   {'description': 'Population weighting needs the population dataset.',
                    'postconditions': {'slot_conditions': {'population_dataset': {'name': 'population_dataset',
                                                                                  'required': True}}},
                    'preconditions': {'slot_conditions': {'centroid_weighting': {'equals_string': 'POPULATION_WEIGHTED',
                                                                                 'name': 'centroid_weighting'}}}},
                   {'description': 'Mixed geocoding needs a breakdown.',
                    'postconditions': {'slot_conditions': {'geocoding_mixed_breakdown': {'name': 'geocoding_mixed_breakdown',
                                                                                         'required': True}}},
                    'preconditions': {'slot_conditions': {'geocoding_precision': {'equals_string': 'MIXED',
                                                                                  'name': 'geocoding_precision'}}}}]})

    spatial_linkage_unit: SpatialLinkageUnitEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    centroid_weighting: Optional[CentroidWeightingEnum] = Field(default=None, description="""Required for any *_CENTROID unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    centroid_areal_unit: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    population_dataset: Optional[str] = Field(default=None, description="""For population-weighted centroids.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    operation: LinkageOperationEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    buffer_radii_m: Optional[list[float]] = Field(default=None, description="""Required for CIRCULAR_BUFFER; list all if several reported.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_mode: Optional[NetworkModeEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_distance_m: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_time_min: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    intersection_min_overlap_pct: Optional[float] = Field(default=None, ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    kernel_bandwidth_m: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    kernel_grid_resolution_m: Optional[float] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    geocoding_precision: Optional[GeocodingPrecisionEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    geocoding_mixed_breakdown: Optional[str] = Field(default=None, description="""For MIXED, e.g. \"80% building, 20% postcode\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    geocoder: Optional[str] = Field(default=None, description="""Geocoding database name and version/release date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    aggregation: AggregationEnum = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    aggregation_n: Optional[int] = Field(default=None, description="""N for MULTI_YEAR_MEAN (years) or PERCENTILE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    participant_coverage_pct: Optional[float] = Field(default=None, ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    coverage_unit: Optional[CoverageUnitEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    study_area_coverage_pct: Optional[float] = Field(default=None, ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    exposure_window: Optional[ExposureWindowEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    exposure_window_years: Optional[int] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    exposure_window_detail: Optional[str] = Field(default=None, description="""Trimester, age range, etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    residential_history: Optional[ResidentialHistoryEnum] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    residential_history_detail: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    linkage_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    relinkages: Optional[list[Relinkage]] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })


class Relinkage(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    date: date = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relinkage']} })
    reason: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['Relinkage']} })


class Person(ConfiguredBaseModel):
    """
    CSV: Creator(s)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage'})

    name: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    email: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    orcid: Optional[URIorCURIE] = Field(default=None, description="""e.g. ORCID:0000-0002-1825-0097""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    role: Optional[str] = Field(default=None, description="""e.g. senior investigator""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })

    @field_validator('email')
    def pattern_email(cls, v):
        pattern=re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid email format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid email format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExposureLinkageCollection.model_rebuild()
ExposureLinkageRecord.model_rebuild()
Cohort.model_rebuild()
ExposureVariable.model_rebuild()
SourceDataset.model_rebuild()
Citation.model_rebuild()
GeographicCoverage.model_rebuild()
SpatialResolution.model_rebuild()
TemporalCoverage.model_rebuild()
ValidationMetric.model_rebuild()
Uncertainty.model_rebuild()
Linkage.model_rebuild()
Relinkage.model_rebuild()
Person.model_rebuild()

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
                         'description': 'Compact identifier using a prefix '
                                        'declared in this schema, e.g. '
                                        'INCHIKEY:..., ENVO:..., MESH:...',
                         'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                         'name': 'CURIE',
                         'title': 'CURIE',
                         'typeof': 'uriorcurie',
                         'uri': 'xsd:anyURI'},
               'PartialDate': {'base': 'str',
                               'description': 'ISO 8601 calendar date at year, '
                                              'month or day precision (YYYY, '
                                              'YYYY-MM or YYYY-MM-DD).',
                               'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                               'name': 'PartialDate',
                               'pattern': '^\\d{4}(-(0[1-9]|1[0-2])(-(0[1-9]|[12]\\d|3[01]))?)?$',
                               'title': 'Partial date',
                               'typeof': 'string',
                               'uri': 'xsd:string'},
               'RegionCode': {'base': 'str',
                              'description': 'ISO 3166-1 alpha-2 country code, or '
                                             'ISO 3166-2 subdivision code (e.g. '
                                             'US-NC).',
                              'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                              'name': 'RegionCode',
                              'pattern': '^(AD|AE|AF|AG|AI|AL|AM|AO|AQ|AR|AS|AT|AU|AW|AX|AZ|BA|BB|BD|BE|BF|BG|BH|BI|BJ|BL|BM|BN|BO|BQ|BR|BS|BT|BV|BW|BY|BZ|CA|CC|CD|CF|CG|CH|CI|CK|CL|CM|CN|CO|CR|CU|CV|CW|CX|CY|CZ|DE|DJ|DK|DM|DO|DZ|EC|EE|EG|EH|ER|ES|ET|FI|FJ|FK|FM|FO|FR|GA|GB|GD|GE|GF|GG|GH|GI|GL|GM|GN|GP|GQ|GR|GS|GT|GU|GW|GY|HK|HM|HN|HR|HT|HU|ID|IE|IL|IM|IN|IO|IQ|IR|IS|IT|JE|JM|JO|JP|KE|KG|KH|KI|KM|KN|KP|KR|KW|KY|KZ|LA|LB|LC|LI|LK|LR|LS|LT|LU|LV|LY|MA|MC|MD|ME|MF|MG|MH|MK|ML|MM|MN|MO|MP|MQ|MR|MS|MT|MU|MV|MW|MX|MY|MZ|NA|NC|NE|NF|NG|NI|NL|NO|NP|NR|NU|NZ|OM|PA|PE|PF|PG|PH|PK|PL|PM|PN|PR|PS|PT|PW|PY|QA|RE|RO|RS|RU|RW|SA|SB|SC|SD|SE|SG|SH|SI|SJ|SK|SL|SM|SN|SO|SR|SS|ST|SV|SX|SY|SZ|TC|TD|TF|TG|TH|TJ|TK|TL|TM|TN|TO|TR|TT|TV|TW|TZ|UA|UG|UM|US|UY|UZ|VA|VC|VE|VG|VI|VN|VU|WF|WS|YE|YT|ZA|ZM|ZW)(-[A-Z0-9]{1,3})?$',
                              'title': 'Region code',
                              'typeof': 'string',
                              'uri': 'xsd:string'},
               'UcumCode': {'base': 'str',
                            'description': 'UCUM case-sensitive code, e.g. ug/m3, '
                                           'ng/m3, [ppb], [ppm], Cel, mm, m/s, '
                                           'W/m2, /km2, %, 1 (dimensionless '
                                           'index). dB(A) has no UCUM code - use '
                                           '"dB" and record the weighting in the '
                                           'exposure variable name.',
                            'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
                            'name': 'UcumCode',
                            'title': 'UCUM code',
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
    """
    Broad domain of an environmental exposure.
    """
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
    """
    Any other domain; give it in domain_other.
    """


class DataOriginEnum(str, Enum):
    """
    How the source exposure data were produced.
    """
    MONITORING_STATION = "MONITORING_STATION"
    LAND_USE_REGRESSION = "LAND_USE_REGRESSION"
    CHEMICAL_TRANSPORT_MODEL = "CHEMICAL_TRANSPORT_MODEL"
    SATELLITE_DERIVED = "SATELLITE_DERIVED"
    PERSONAL_MONITOR = "PERSONAL_MONITOR"
    QUESTIONNAIRE = "QUESTIONNAIRE"
    ADMINISTRATIVE_RECORD = "ADMINISTRATIVE_RECORD"
    REANALYSIS = "REANALYSIS"
    """
    Reanalysis products such as ERA5. Added because they were otherwise unclassifiable.
    """
    OTHER = "OTHER"


class GeographicScopeEnum(str, Enum):
    """
    Kind of geographic coverage.
    """
    COUNTRIES_OR_REGIONS = "COUNTRIES_OR_REGIONS"
    """
    Listed countries or subdivisions; give them in regions.
    """
    EU27 = "EU27"
    """
    The 27 EU member states.
    """
    GLOBAL = "GLOBAL"
    """
    Worldwide coverage.
    """


class SpatialResolutionTypeEnum(str, Enum):
    """
    Kind of spatial support of a source dataset.
    """
    GRID_METRIC = "GRID_METRIC"
    """
    Regular grid with cell size in metres.
    """
    GRID_DEGREE = "GRID_DEGREE"
    """
    Regular grid with cell size in degrees.
    """
    ADMINISTRATIVE_UNIT = "ADMINISTRATIVE_UNIT"
    """
    Values per administrative area.
    """
    POINT_ADDRESS = "POINT_ADDRESS"
    """
    Values at address points.
    """
    POINT_GPS = "POINT_GPS"
    """
    Values at GPS points.
    """


class TemporalResolutionEnum(str, Enum):
    """
    Temporal resolution of a source dataset.
    """
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
    """
    Static snapshots refreshed at an interval; give it in update_frequency.
    """


class ValidationMetricEnum(str, Enum):
    """
    Validation statistic.
    """
    R2 = "R2"
    """
    Coefficient of determination.
    """
    RMSE = "RMSE"
    """
    Root mean squared error.
    """
    NRMSE_PCT = "NRMSE_PCT"
    """
    Normalised root mean squared error, in percent.
    """
    MEAN_BIAS = "MEAN_BIAS"
    """
    Mean bias.
    """
    RELATIVE_BIAS_PCT = "RELATIVE_BIAS_PCT"
    """
    Relative bias, in percent.
    """
    PEARSON_R = "PEARSON_R"
    """
    Pearson correlation coefficient.
    """


class ValidationDesignEnum(str, Enum):
    """
    How a validation was carried out.
    """
    LOOCV_SPATIAL = "LOOCV_SPATIAL"
    """
    Leave-one-out cross-validation over sites.
    """
    INDEPENDENT_TEST_SET_SPATIAL = "INDEPENDENT_TEST_SET_SPATIAL"
    """
    Validation against held-out sites.
    """
    TEMPORAL = "TEMPORAL"
    """
    Validation against held-out time periods.
    """
    OVERALL = "OVERALL"
    """
    Validation reported without a stated design.
    """
    GROUND_MONITOR_COMPARISON = "GROUND_MONITOR_COMPARISON"
    """
    Comparison against ground monitors.
    """


class UncertaintyTypeEnum(str, Enum):
    """
    Form in which uncertainty is available.
    """
    NOT_AVAILABLE = "NOT_AVAILABLE"
    SD_PER_UNIT = "SD_PER_UNIT"
    """
    Standard deviation per spatial unit.
    """
    PREDICTION_INTERVAL_95 = "PREDICTION_INTERVAL_95"
    """
    95% prediction interval.
    """
    FULL_PREDICTIVE_DISTRIBUTION = "FULL_PREDICTIVE_DISTRIBUTION"
    MODEL_LEVEL_RMSE_ONLY = "MODEL_LEVEL_RMSE_ONLY"
    """
    Only a model-level RMSE is available.
    """


class SpatialLinkageUnitEnum(str, Enum):
    """
    Participant location used for the linkage.
    """
    GEOCODED_ADDRESS = "GEOCODED_ADDRESS"
    GPS_COORDINATE = "GPS_COORDINATE"
    POSTCODE_CENTROID = "POSTCODE_CENTROID"
    CENSUS_TRACT_CENTROID = "CENSUS_TRACT_CENTROID"
    LSOA_CENTROID = "LSOA_CENTROID"
    """
    Centroid of a Lower Layer Super Output Area (England and Wales).
    """
    MUNICIPALITY_CENTROID = "MUNICIPALITY_CENTROID"
    OTHER_AREAL_CENTROID = "OTHER_AREAL_CENTROID"
    GRID_CELL_CONTAINING_ADDRESS = "GRID_CELL_CONTAINING_ADDRESS"


class CentroidWeightingEnum(str, Enum):
    """
    How an areal centroid was computed.
    """
    GEOMETRIC = "GEOMETRIC"
    POPULATION_WEIGHTED = "POPULATION_WEIGHTED"
    """
    Population-weighted centroid; give the population dataset.
    """
    AREA_WEIGHTED = "AREA_WEIGHTED"


class LinkageOperationEnum(str, Enum):
    """
    GIS operation used to assign exposure values to locations.
    """
    POINT_IN_POLYGON = "POINT_IN_POLYGON"
    CIRCULAR_BUFFER = "CIRCULAR_BUFFER"
    """
    Euclidean buffer; give the radii in buffer_radii_m.
    """
    NETWORK_BUFFER = "NETWORK_BUFFER"
    """
    Street-network buffer; give network_mode.
    """
    NEAREST_FEATURE = "NEAREST_FEATURE"
    AREAL_INTERPOLATION = "AREAL_INTERPOLATION"
    INTERSECTION = "INTERSECTION"
    KERNEL_DENSITY_WEIGHTED = "KERNEL_DENSITY_WEIGHTED"
    """
    Kernel-weighted surface; give kernel_bandwidth_m.
    """
    ADMINISTRATIVE_ASSIGNMENT = "ADMINISTRATIVE_ASSIGNMENT"


class NetworkModeEnum(str, Enum):
    """
    Travel mode for a network buffer.
    """
    WALKING = "WALKING"
    CYCLING = "CYCLING"
    DRIVING = "DRIVING"
    PUBLIC_TRANSPORT = "PUBLIC_TRANSPORT"


class GeocodingPrecisionEnum(str, Enum):
    """
    Precision of participant geocodes.
    """
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
    """
    Several levels; give the shares in geocoding_mixed_breakdown.
    """
    UNKNOWN = "UNKNOWN"


class AggregationEnum(str, Enum):
    """
    Summary statistic applied to exposure values.
    """
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
    """
    Mean over N years; give N in aggregation_n.
    """
    CUMULATIVE_SUM = "CUMULATIVE_SUM"
    PERCENTILE = "PERCENTILE"
    """
    The Nth percentile; give N in aggregation_n.
    """
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
    """
    Unit that a coverage percentage counts.
    """
    PARTICIPANTS = "PARTICIPANTS"
    HOUSEHOLDS = "HOUSEHOLDS"
    CLINICAL_SITES = "CLINICAL_SITES"
    HOSPITALS = "HOSPITALS"
    GEOGRAPHIC_UNITS = "GEOGRAPHIC_UNITS"


class ExposureWindowEnum(str, Enum):
    """
    Period of exposure that linked values represent.
    """
    YEAR_BEFORE_RECRUITMENT = "YEAR_BEFORE_RECRUITMENT"
    N_YEARS_BEFORE_INDEX = "N_YEARS_BEFORE_INDEX"
    """
    N years before an index date; give N in exposure_window_years.
    """
    PRENATAL = "PRENATAL"
    PERICONCEPTION = "PERICONCEPTION"
    INFANCY = "INFANCY"
    EARLY_CHILDHOOD = "EARLY_CHILDHOOD"
    ADOLESCENCE = "ADOLESCENCE"
    LIFETIME_CUMULATIVE = "LIFETIME_CUMULATIVE"
    TIME_VARYING_ANNUAL = "TIME_VARYING_ANNUAL"
    CRITICAL_WINDOW = "CRITICAL_WINDOW"


class ResidentialHistoryEnum(str, Enum):
    """
    Extent to which residential moves were accounted for.
    """
    BASELINE_ONLY = "BASELINE_ONLY"
    FULL_HISTORY = "FULL_HISTORY"
    PARTIAL_HISTORY = "PARTIAL_HISTORY"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"



class ExposureLinkageCollection(ConfiguredBaseModel):
    """
    Container so that one file can hold many exposure linkage records.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'title': 'Exposure linkage collection',
         'tree_root': True})

    records: list[ExposureLinkageRecord] = Field(default=..., title="Records", description="""The exposure linkage records in this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageCollection']} })


class ExposureLinkageRecord(ConfiguredBaseModel):
    """
    One exposure variable linked to the participants of one cohort.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'title': 'Exposure linkage record'})

    id: str = Field(default=..., title="Record identifier", description="""Stable record identifier, e.g. UKB-NO2-ELAPSE-2010.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    cohort: Cohort = Field(default=..., title="Cohort", description="""The cohort or study whose participants received the exposure values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    exposure: ExposureVariable = Field(default=..., title="Exposure", description="""The exposure variable that was linked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    source_data: SourceDataset = Field(default=..., title="Source data", description="""The upstream exposure product the values were taken from.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    linkage: Linkage = Field(default=..., title="Linkage", description="""How exposure values were assigned to participants.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord']} })
    creators: Optional[list[Person]] = Field(default=None, title="Creator(s)", description="""People responsible for producing this linkage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureLinkageRecord'], 'recommended': True} })


class Cohort(ConfiguredBaseModel):
    """
    The cohort or study whose participants were linked. Replaces the CSV fields \"Cohort / Study Name\" and \"Country of Participant Data Collection\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage', 'title': 'Cohort'})

    name: str = Field(default=..., title="Cohort / Study Name", description="""Full name of the cohort or study, e.g. UK Biobank.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    acronym: str = Field(default=..., title="Cohort acronym", description="""Short name, e.g. UKB. Split out of the old \"Name (ACRONYM)\" string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })
    collection_countries: list[CountryCodeEnum] = Field(default=..., title="Country of Participant Data Collection", description="""Countries in which participant data were collected, as ISO 3166-1 alpha-2 codes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort']} })


class ExposureVariable(ConfiguredBaseModel):
    """
    The environmental exposure that was linked. Replaces the CSV fields \"Exposure Domain\", \"Exposure Variable Name\", \"Ontology / Taxonomy Term ID\" and \"Unit of Measure\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'OTHER domain must be specified.',
                    'postconditions': {'slot_conditions': {'domain_other': {'name': 'domain_other',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'domain': {'equals_string': 'OTHER',
                                                                     'name': 'domain'}}}}],
         'title': 'Exposure variable'})

    domain: ExposureDomainEnum = Field(default=..., title="Exposure Domain", description="""Broad exposure domain.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })
    domain_other: Optional[str] = Field(default=None, title="Exposure Domain (other)", description="""Free-text domain. Required when domain = OTHER.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })
    name: str = Field(default=..., title="Exposure Variable Name", description="""Descriptive term for the variable, e.g. NO2, PM2.5, Lden, NDVI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    ontology_terms: Optional[list[URIorCURIE]] = Field(default=None, title="Ontology / Taxonomy Term ID", description="""Resolvable identifiers for the exposure. Chemicals: INCHIKEY (preferred), PUBCHEM, DTXSID, CAS. Physical or environmental exposures: ExO, ENVO, MESH. Leave empty if no term exists.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable'], 'recommended': True} })
    unit: Optional[str] = Field(default=None, title="Unit of Measure", description="""UCUM code for the unit of the linked values. Omit for categorical variables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })
    is_categorical: Optional[bool] = Field(default=None, title="Is categorical", description="""True if the variable takes categorical rather than numeric values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable']} })


class SourceDataset(ConfiguredBaseModel):
    """
    The upstream exposure product (model, satellite product, monitoring network, ...).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Periodic update needs a frequency.',
                    'postconditions': {'slot_conditions': {'update_frequency': {'name': 'update_frequency',
                                                                                'required': True}}},
                    'preconditions': {'slot_conditions': {'temporal_resolution': {'equals_string': 'PERIODIC_UPDATE',
                                                                                  'name': 'temporal_resolution'}}}}],
         'title': 'Source dataset'})

    origin: DataOriginEnum = Field(default=..., title="Origin of the Data", description="""How the source exposure data were produced.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    dataset_name: str = Field(default=..., title="Model / Dataset Name", description="""Name of the model or dataset, e.g. ELAPSE LUR, ERA5, MODIS MOD13A3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    dataset_version: str = Field(default=..., title="Model / Dataset Version", description="""Version number or release year, e.g. 2.0, 006, 2023.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    citations: list[Citation] = Field(default=..., title="Data Source Citation / URL", description="""Citations for the source dataset and the methods used to produce it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    geographic_coverage: GeographicCoverage = Field(default=..., title="Geographic Coverage", description="""Area covered by the source dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    spatial_resolution: SpatialResolution = Field(default=..., title="Spatial Resolution", description="""Spatial resolution of the source dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    temporal_coverage: TemporalCoverage = Field(default=..., title="Date Coverage", description="""Period covered by the source dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    temporal_resolution: TemporalResolutionEnum = Field(default=..., title="Temporal Resolution", description="""Temporal resolution of the source dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    update_frequency: Optional[str] = Field(default=None, title="Update frequency", description="""For PERIODIC_UPDATE, the update interval as an ISO 8601 duration, e.g. P5Y.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    validation_metrics: Optional[list[ValidationMetric]] = Field(default=None, title="Validation Status", description="""Reported validation metrics. An empty list with validation_reported = false means the dataset was not validated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset'], 'recommended': True} })
    validation_reported: Optional[bool] = Field(default=None, title="Validation reported", description="""True if the dataset producers report a validation of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset']} })
    uncertainty: Optional[Uncertainty] = Field(default=None, title="Uncertainty", description="""Uncertainty information available for the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceDataset'], 'recommended': True} })

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
    """
    A reference to the source data or its documentation. At least one of doi, url or text is required.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'doi': {'name': 'doi', 'required': True}}},
                    {'slot_conditions': {'url': {'name': 'url', 'required': True}}},
                    {'slot_conditions': {'text': {'name': 'text', 'required': True}}}],
         'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'title': 'Citation'})

    doi: Optional[str] = Field(default=None, title="DOI", description="""Bare DOI, without the doi: prefix or resolver URL, e.g. 10.1234/abcd.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    url: Optional[str] = Field(default=None, title="URL", description="""Web address of the source or its documentation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    accessed: Optional[date] = Field(default=None, title="Accessed", description="""Date the URL was accessed. Required when url is given without a DOI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    text: Optional[str] = Field(default=None, title="Citation text", description="""Free-text citation, for sources without a DOI or URL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })
    used_for_linkage: Optional[bool] = Field(default=None, title="Used for linkage", description="""True if this is the source actually used for the linkage. Replaces the old \"*\" marker.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Citation']} })

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
    """
    Area covered by a source dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Country/region scope needs region codes.',
                    'postconditions': {'slot_conditions': {'regions': {'name': 'regions',
                                                                       'required': True}}},
                    'preconditions': {'slot_conditions': {'scope': {'equals_string': 'COUNTRIES_OR_REGIONS',
                                                                    'name': 'scope'}}}}],
         'title': 'Geographic coverage'})

    scope: GeographicScopeEnum = Field(default=..., title="Scope", description="""Kind of coverage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })
    regions: Optional[list[str]] = Field(default=None, title="Regions", description="""ISO 3166-1 / ISO 3166-2 codes. Required when scope = COUNTRIES_OR_REGIONS.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })
    description: Optional[str] = Field(default=None, title="Coverage description", description="""Optional note, e.g. \"UK-wide\", \"multiple provinces\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeographicCoverage']} })


class SpatialResolution(ConfiguredBaseModel):
    """
    Spatial resolution of a source dataset, as numbers rather than strings such as \"100 m x 100 m\".
    """
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
                                                                   'name': 'type'}}}}],
         'title': 'Spatial resolution'})

    type: SpatialResolutionTypeEnum = Field(default=..., title="Resolution type", description="""Kind of spatial support.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution', 'Uncertainty']} })
    cell_width: Optional[float] = Field(default=None, title="Cell width", description="""Grid cell width; metres for GRID_METRIC, degrees for GRID_DEGREE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    cell_height: Optional[float] = Field(default=None, title="Cell height", description="""Grid cell height; metres for GRID_METRIC, degrees for GRID_DEGREE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    admin_unit_name: Optional[str] = Field(default=None, title="Administrative unit name", description="""For ADMINISTRATIVE_UNIT, the unit type, e.g. LSOA, census tract.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })
    admin_unit_approx_population: Optional[int] = Field(default=None, title="Administrative unit approximate population", description="""Typical population of one administrative unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution']} })


class TemporalCoverage(ConfiguredBaseModel):
    """
    Period covered by a source dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'rules': [{'description': 'Ongoing datasets need a last-updated date.',
                    'postconditions': {'slot_conditions': {'last_updated': {'name': 'last_updated',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'ongoing': {'equals_string': 'true',
                                                                      'name': 'ongoing'}}}}],
         'title': 'Temporal coverage'})

    start: str = Field(default=..., title="Date Coverage - Start", description="""First date covered, as an ISO 8601 partial date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    end: Optional[str] = Field(default=None, title="Date Coverage - End", description="""Last date covered, as an ISO 8601 partial date. Omit when ongoing = true.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    ongoing: Optional[bool] = Field(default=None, title="Ongoing", description="""True if the dataset is still being extended. Replaces the magic string \"Ongoing\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })
    last_updated: Optional[str] = Field(default=None, title="Last updated", description="""Date of the most recent update. Required when ongoing = true.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalCoverage']} })


class ValidationMetric(ConfiguredBaseModel):
    """
    One reported validation metric of a source dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'title': 'Validation metric'})

    metric: ValidationMetricEnum = Field(default=..., title="Metric", description="""The validation statistic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric']} })
    validation_design: Optional[ValidationDesignEnum] = Field(default=None, title="Validation design", description="""How the validation was carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric']} })
    value: float = Field(default=..., title="Value", description="""Value of the statistic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric', 'Uncertainty']} })
    unit: Optional[str] = Field(default=None, title="Unit", description="""UCUM code, for RMSE and mean bias. Omit for R2, r and percentages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })


class Uncertainty(ConfiguredBaseModel):
    """
    Uncertainty information for a source dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage',
         'title': 'Uncertainty'})

    type: UncertaintyTypeEnum = Field(default=..., title="Uncertainty type", description="""Form in which uncertainty is available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SpatialResolution', 'Uncertainty']} })
    value: Optional[float] = Field(default=None, title="Value", description="""Point value of the uncertainty measure, if a single value applies.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ValidationMetric', 'Uncertainty']} })
    lower: Optional[float] = Field(default=None, title="Lower bound", description="""Lower bound of the uncertainty interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })
    upper: Optional[float] = Field(default=None, title="Upper bound", description="""Upper bound of the uncertainty interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })
    unit: Optional[str] = Field(default=None, title="Unit", description="""UCUM code for value, lower and upper.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExposureVariable', 'ValidationMetric', 'Uncertainty']} })
    carried_to_participant_level: Optional[bool] = Field(default=None, title="Carried to participant level", description="""True if uncertainty is propagated to the participant-level exposure values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Uncertainty']} })


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
                                                                                  'name': 'geocoding_precision'}}}}],
         'title': 'Linkage'})

    spatial_linkage_unit: SpatialLinkageUnitEnum = Field(default=..., title="Spatial Linkage Unit", description="""Participant location used for the linkage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    centroid_weighting: Optional[CentroidWeightingEnum] = Field(default=None, title="Centroid weighting", description="""How the centroid was computed. Required for any *_CENTROID unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    centroid_areal_unit: Optional[str] = Field(default=None, title="Centroid areal unit", description="""The areal unit the centroid represents, e.g. \"output area\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    population_dataset: Optional[str] = Field(default=None, title="Population dataset", description="""Population dataset used for POPULATION_WEIGHTED centroids.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    operation: LinkageOperationEnum = Field(default=..., title="Spatial Linkage Operation", description="""GIS operation used to assign values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    buffer_radii_m: Optional[list[float]] = Field(default=None, title="Buffer Distance", description="""Buffer radii in metres. Required for CIRCULAR_BUFFER; list all radii if several were reported.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_mode: Optional[NetworkModeEnum] = Field(default=None, title="Network mode", description="""Travel mode for NETWORK_BUFFER.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_distance_m: Optional[float] = Field(default=None, title="Network distance (m)", description="""Network buffer distance in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    network_time_min: Optional[float] = Field(default=None, title="Network time (min)", description="""Network buffer travel time in minutes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    intersection_min_overlap_pct: Optional[float] = Field(default=None, title="Intersection minimum overlap (%)", description="""Minimum areal overlap, in percent, for INTERSECTION.""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    kernel_bandwidth_m: Optional[float] = Field(default=None, title="Kernel bandwidth (m)", description="""Kernel bandwidth in metres. Required for KERNEL_DENSITY_WEIGHTED.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    kernel_grid_resolution_m: Optional[float] = Field(default=None, title="Kernel grid resolution (m)", description="""Output grid resolution of the kernel density surface, in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    geocoding_precision: Optional[GeocodingPrecisionEnum] = Field(default=None, title="Geocoding Precision", description="""Precision of participant geocodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    geocoding_mixed_breakdown: Optional[str] = Field(default=None, title="Geocoding mixed breakdown", description="""For MIXED precision, the share of each level, e.g. \"80% building, 20% postcode\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    geocoder: Optional[str] = Field(default=None, title="Geocoding Database Version", description="""Geocoding database name and version or release date.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    aggregation: AggregationEnum = Field(default=..., title="Summary Statistic / Aggregation", description="""Summary statistic applied to the exposure values. Buffer geometry is recorded once, under operation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    aggregation_n: Optional[int] = Field(default=None, title="Aggregation N", description="""N for MULTI_YEAR_MEAN (years) or PERCENTILE (the percentile).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    participant_coverage_pct: Optional[float] = Field(default=None, title="Missing Data / Coverage", description="""Percentage (0-100) of coverage units that received an exposure value.""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    coverage_unit: Optional[CoverageUnitEnum] = Field(default=None, title="Coverage unit", description="""Unit that participant_coverage_pct counts.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    study_area_coverage_pct: Optional[float] = Field(default=None, title="Study area coverage (%)", description="""Percentage (0-100) of the study area covered by the source dataset.""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    exposure_window: Optional[ExposureWindowEnum] = Field(default=None, title="Exposure Window", description="""Period of exposure the linked values represent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    exposure_window_years: Optional[int] = Field(default=None, title="Exposure window (years)", description="""Length of the exposure window in years, e.g. N for N_YEARS_BEFORE_INDEX.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    exposure_window_detail: Optional[str] = Field(default=None, title="Exposure window detail", description="""Further detail, e.g. trimester or age range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    residential_history: Optional[ResidentialHistoryEnum] = Field(default=None, title="Residential History", description="""Extent to which residential moves were accounted for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    residential_history_detail: Optional[str] = Field(default=None, title="Residential history detail", description="""Free-text detail on how residential history was handled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })
    linkage_date: Optional[date] = Field(default=None, title="Linkage Date", description="""Date the linkage was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage'], 'recommended': True} })
    relinkages: Optional[list[Relinkage]] = Field(default=None, title="Relinkages", description="""Later re-runs of the linkage, e.g. after a geocoder update.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Linkage']} })


class Relinkage(ConfiguredBaseModel):
    """
    A later re-run of a linkage.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage', 'title': 'Relinkage'})

    date: date = Field(default=..., title="Relinkage date", description="""Date of the re-run.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relinkage']} })
    reason: str = Field(default=..., title="Reason", description="""Why the linkage was re-run, e.g. geocoder update.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Relinkage']} })


class Person(ConfiguredBaseModel):
    """
    A creator of the linkage. Replaces the CSV field \"Creator(s)\".
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ga4gh/exposure-linkage', 'title': 'Person'})

    name: Optional[str] = Field(default=None, title="Name", description="""Full name of the person.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Cohort', 'ExposureVariable', 'Person']} })
    email: Optional[str] = Field(default=None, title="Email", description="""Contact email address.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    orcid: Optional[URIorCURIE] = Field(default=None, title="ORCID", description="""ORCID identifier as a CURIE, e.g. ORCID:0000-0002-1825-0097.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    role: Optional[str] = Field(default=None, title="Role", description="""Role in producing the linkage, e.g. senior investigator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })

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

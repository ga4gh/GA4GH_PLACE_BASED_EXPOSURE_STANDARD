# Auto generated from exposure_linkage.yaml by pythongen.py version: 0.0.1
# Schema: exposure_linkage
#
# id: https://w3id.org/ga4gh/exposure-linkage
# description: Describes how an environmental exposure dataset was linked to cohort participants. One ExposureLinkageRecord = one exposure variable linked in one cohort. Converted from "Implementation 1 - GA4GH Metadata Schema".
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate

metamodel_version = "1.12.0"
version = "0.1.0"

# Namespaces
CAS = CurieNamespace('CAS', 'https://identifiers.org/cas:')
DTXSID = CurieNamespace('DTXSID', 'https://comptox.epa.gov/dashboard/chemical/details/')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
INCHIKEY = CurieNamespace('INCHIKEY', 'https://identifiers.org/inchikey:')
MESH = CurieNamespace('MESH', 'http://id.nlm.nih.gov/mesh/')
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PUBCHEM = CurieNamespace('PUBCHEM', 'http://rdf.ncbi.nlm.nih.gov/pubchem/compound/CID')
EXPO = CurieNamespace('expo', 'https://w3id.org/ga4gh/exposure-linkage/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EXPO


# Types
class RegionCode(String):
    """ ISO 3166-1 alpha-2 or ISO 3166-2 subdivision (e.g. US-NC). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "RegionCode"
    type_model_uri = EXPO.RegionCode


class PartialDate(String):
    """ ISO 8601 YYYY, YYYY-MM or YYYY-MM-DD. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "PartialDate"
    type_model_uri = EXPO.PartialDate


class CURIE(Uriorcurie):
    """ Compact identifier, e.g. INCHIKEY:..., ENVO:..., MESH:... """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "CURIE"
    type_model_uri = EXPO.CURIE


class UcumCode(String):
    """ UCUM case-sensitive code, e.g. ug/m3, ng/m3, [ppb], [ppm], Cel, mm, m/s, W/m2, /km2, %, 1 (dimensionless index). dB(A) has no UCUM code - use "dB" with weighting recorded in exposure_variable. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UcumCode"
    type_model_uri = EXPO.UcumCode


# Class references
class ExposureLinkageRecordId(extended_str):
    pass


@dataclass(repr=False)
class ExposureLinkageCollection(YAMLRoot):
    """
    Container so one file can hold many records.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["ExposureLinkageCollection"]
    class_class_curie: ClassVar[str] = "expo:ExposureLinkageCollection"
    class_name: ClassVar[str] = "ExposureLinkageCollection"
    class_model_uri: ClassVar[URIRef] = EXPO.ExposureLinkageCollection

    records: Union[dict[Union[str, ExposureLinkageRecordId], Union[dict, "ExposureLinkageRecord"]], list[Union[dict, "ExposureLinkageRecord"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.records):
            self.MissingRequiredField("records")
        self._normalize_inlined_as_list(slot_name="records", slot_type=ExposureLinkageRecord, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureLinkageRecord(YAMLRoot):
    """
    One exposure variable linked to one cohort.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["ExposureLinkageRecord"]
    class_class_curie: ClassVar[str] = "expo:ExposureLinkageRecord"
    class_name: ClassVar[str] = "ExposureLinkageRecord"
    class_model_uri: ClassVar[URIRef] = EXPO.ExposureLinkageRecord

    id: Union[str, ExposureLinkageRecordId] = None
    cohort: Union[dict, "Cohort"] = None
    exposure: Union[dict, "ExposureVariable"] = None
    source_data: Union[dict, "SourceDataset"] = None
    linkage: Union[dict, "Linkage"] = None
    creators: Optional[Union[Union[dict, "Person"], list[Union[dict, "Person"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureLinkageRecordId):
            self.id = ExposureLinkageRecordId(self.id)

        if self._is_empty(self.cohort):
            self.MissingRequiredField("cohort")
        if not isinstance(self.cohort, Cohort):
            self.cohort = Cohort(**as_dict(self.cohort))

        if self._is_empty(self.exposure):
            self.MissingRequiredField("exposure")
        if not isinstance(self.exposure, ExposureVariable):
            self.exposure = ExposureVariable(**as_dict(self.exposure))

        if self._is_empty(self.source_data):
            self.MissingRequiredField("source_data")
        if not isinstance(self.source_data, SourceDataset):
            self.source_data = SourceDataset(**as_dict(self.source_data))

        if self._is_empty(self.linkage):
            self.MissingRequiredField("linkage")
        if not isinstance(self.linkage, Linkage):
            self.linkage = Linkage(**as_dict(self.linkage))

        if not isinstance(self.creators, list):
            self.creators = [self.creators] if self.creators is not None else []
        self.creators = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.creators]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Cohort(YAMLRoot):
    """
    CSV: Cohort / Study Name; Country of Participant Data Collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Cohort"]
    class_class_curie: ClassVar[str] = "expo:Cohort"
    class_name: ClassVar[str] = "Cohort"
    class_model_uri: ClassVar[URIRef] = EXPO.Cohort

    name: str = None
    acronym: str = None
    collection_countries: Union[Union[str, "CountryCodeEnum"], list[Union[str, "CountryCodeEnum"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.acronym):
            self.MissingRequiredField("acronym")
        if not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self._is_empty(self.collection_countries):
            self.MissingRequiredField("collection_countries")
        if not isinstance(self.collection_countries, list):
            self.collection_countries = [self.collection_countries] if self.collection_countries is not None else []
        self.collection_countries = [v if isinstance(v, CountryCodeEnum) else CountryCodeEnum(v) for v in self.collection_countries]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureVariable(YAMLRoot):
    """
    CSV: Exposure Domain; Exposure Variable Name; Ontology Term ID; Unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["ExposureVariable"]
    class_class_curie: ClassVar[str] = "expo:ExposureVariable"
    class_name: ClassVar[str] = "ExposureVariable"
    class_model_uri: ClassVar[URIRef] = EXPO.ExposureVariable

    domain: Union[str, "ExposureDomainEnum"] = None
    name: str = None
    domain_other: Optional[str] = None
    ontology_terms: Optional[Union[Union[str, CURIE], list[Union[str, CURIE]]]] = empty_list()
    unit: Optional[Union[str, UcumCode]] = None
    is_categorical: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, ExposureDomainEnum):
            self.domain = ExposureDomainEnum(self.domain)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.domain_other is not None and not isinstance(self.domain_other, str):
            self.domain_other = str(self.domain_other)

        if not isinstance(self.ontology_terms, list):
            self.ontology_terms = [self.ontology_terms] if self.ontology_terms is not None else []
        self.ontology_terms = [v if isinstance(v, CURIE) else CURIE(v) for v in self.ontology_terms]

        if self.unit is not None and not isinstance(self.unit, UcumCode):
            self.unit = UcumCode(self.unit)

        if self.is_categorical is not None and not isinstance(self.is_categorical, Bool):
            self.is_categorical = Bool(self.is_categorical)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceDataset(YAMLRoot):
    """
    The upstream exposure product (model, satellite, monitors...).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["SourceDataset"]
    class_class_curie: ClassVar[str] = "expo:SourceDataset"
    class_name: ClassVar[str] = "SourceDataset"
    class_model_uri: ClassVar[URIRef] = EXPO.SourceDataset

    origin: Union[str, "DataOriginEnum"] = None
    dataset_name: str = None
    dataset_version: str = None
    citations: Union[Union[dict, "Citation"], list[Union[dict, "Citation"]]] = None
    geographic_coverage: Union[dict, "GeographicCoverage"] = None
    spatial_resolution: Union[dict, "SpatialResolution"] = None
    temporal_coverage: Union[dict, "TemporalCoverage"] = None
    temporal_resolution: Union[str, "TemporalResolutionEnum"] = None
    update_frequency: Optional[str] = None
    validation_metrics: Optional[Union[Union[dict, "ValidationMetric"], list[Union[dict, "ValidationMetric"]]]] = empty_list()
    validation_reported: Optional[Union[bool, Bool]] = None
    uncertainty: Optional[Union[dict, "Uncertainty"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.origin):
            self.MissingRequiredField("origin")
        if not isinstance(self.origin, DataOriginEnum):
            self.origin = DataOriginEnum(self.origin)

        if self._is_empty(self.dataset_name):
            self.MissingRequiredField("dataset_name")
        if not isinstance(self.dataset_name, str):
            self.dataset_name = str(self.dataset_name)

        if self._is_empty(self.dataset_version):
            self.MissingRequiredField("dataset_version")
        if not isinstance(self.dataset_version, str):
            self.dataset_version = str(self.dataset_version)

        if self._is_empty(self.citations):
            self.MissingRequiredField("citations")
        if not isinstance(self.citations, list):
            self.citations = [self.citations] if self.citations is not None else []
        self.citations = [v if isinstance(v, Citation) else Citation(**as_dict(v)) for v in self.citations]

        if self._is_empty(self.geographic_coverage):
            self.MissingRequiredField("geographic_coverage")
        if not isinstance(self.geographic_coverage, GeographicCoverage):
            self.geographic_coverage = GeographicCoverage(**as_dict(self.geographic_coverage))

        if self._is_empty(self.spatial_resolution):
            self.MissingRequiredField("spatial_resolution")
        if not isinstance(self.spatial_resolution, SpatialResolution):
            self.spatial_resolution = SpatialResolution(**as_dict(self.spatial_resolution))

        if self._is_empty(self.temporal_coverage):
            self.MissingRequiredField("temporal_coverage")
        if not isinstance(self.temporal_coverage, TemporalCoverage):
            self.temporal_coverage = TemporalCoverage(**as_dict(self.temporal_coverage))

        if self._is_empty(self.temporal_resolution):
            self.MissingRequiredField("temporal_resolution")
        if not isinstance(self.temporal_resolution, TemporalResolutionEnum):
            self.temporal_resolution = TemporalResolutionEnum(self.temporal_resolution)

        if self.update_frequency is not None and not isinstance(self.update_frequency, str):
            self.update_frequency = str(self.update_frequency)

        self._normalize_inlined_as_list(slot_name="validation_metrics", slot_type=ValidationMetric, key_name="metric", keyed=False)

        if self.validation_reported is not None and not isinstance(self.validation_reported, Bool):
            self.validation_reported = Bool(self.validation_reported)

        if self.uncertainty is not None and not isinstance(self.uncertainty, Uncertainty):
            self.uncertainty = Uncertainty(**as_dict(self.uncertainty))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citation(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Citation"]
    class_class_curie: ClassVar[str] = "expo:Citation"
    class_name: ClassVar[str] = "Citation"
    class_model_uri: ClassVar[URIRef] = EXPO.Citation

    doi: Optional[str] = None
    url: Optional[Union[str, URI]] = None
    accessed: Optional[Union[str, XSDDate]] = None
    text: Optional[str] = None
    used_for_linkage: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.accessed is not None and not isinstance(self.accessed, XSDDate):
            self.accessed = XSDDate(self.accessed)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        if self.used_for_linkage is not None and not isinstance(self.used_for_linkage, Bool):
            self.used_for_linkage = Bool(self.used_for_linkage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeographicCoverage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["GeographicCoverage"]
    class_class_curie: ClassVar[str] = "expo:GeographicCoverage"
    class_name: ClassVar[str] = "GeographicCoverage"
    class_model_uri: ClassVar[URIRef] = EXPO.GeographicCoverage

    scope: Union[str, "GeographicScopeEnum"] = None
    regions: Optional[Union[Union[str, RegionCode], list[Union[str, RegionCode]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, GeographicScopeEnum):
            self.scope = GeographicScopeEnum(self.scope)

        if not isinstance(self.regions, list):
            self.regions = [self.regions] if self.regions is not None else []
        self.regions = [v if isinstance(v, RegionCode) else RegionCode(v) for v in self.regions]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpatialResolution(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["SpatialResolution"]
    class_class_curie: ClassVar[str] = "expo:SpatialResolution"
    class_name: ClassVar[str] = "SpatialResolution"
    class_model_uri: ClassVar[URIRef] = EXPO.SpatialResolution

    type: Union[str, "SpatialResolutionTypeEnum"] = None
    cell_width: Optional[float] = None
    cell_height: Optional[float] = None
    admin_unit_name: Optional[str] = None
    admin_unit_approx_population: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, SpatialResolutionTypeEnum):
            self.type = SpatialResolutionTypeEnum(self.type)

        if self.cell_width is not None and not isinstance(self.cell_width, float):
            self.cell_width = float(self.cell_width)

        if self.cell_height is not None and not isinstance(self.cell_height, float):
            self.cell_height = float(self.cell_height)

        if self.admin_unit_name is not None and not isinstance(self.admin_unit_name, str):
            self.admin_unit_name = str(self.admin_unit_name)

        if self.admin_unit_approx_population is not None and not isinstance(self.admin_unit_approx_population, int):
            self.admin_unit_approx_population = int(self.admin_unit_approx_population)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemporalCoverage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["TemporalCoverage"]
    class_class_curie: ClassVar[str] = "expo:TemporalCoverage"
    class_name: ClassVar[str] = "TemporalCoverage"
    class_model_uri: ClassVar[URIRef] = EXPO.TemporalCoverage

    start: Union[str, PartialDate] = None
    end: Optional[Union[str, PartialDate]] = None
    ongoing: Optional[Union[bool, Bool]] = None
    last_updated: Optional[Union[str, PartialDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start):
            self.MissingRequiredField("start")
        if not isinstance(self.start, PartialDate):
            self.start = PartialDate(self.start)

        if self.end is not None and not isinstance(self.end, PartialDate):
            self.end = PartialDate(self.end)

        if self.ongoing is not None and not isinstance(self.ongoing, Bool):
            self.ongoing = Bool(self.ongoing)

        if self.last_updated is not None and not isinstance(self.last_updated, PartialDate):
            self.last_updated = PartialDate(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ValidationMetric(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["ValidationMetric"]
    class_class_curie: ClassVar[str] = "expo:ValidationMetric"
    class_name: ClassVar[str] = "ValidationMetric"
    class_model_uri: ClassVar[URIRef] = EXPO.ValidationMetric

    metric: Union[str, "ValidationMetricEnum"] = None
    value: float = None
    validation_design: Optional[Union[str, "ValidationDesignEnum"]] = None
    unit: Optional[Union[str, UcumCode]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.metric):
            self.MissingRequiredField("metric")
        if not isinstance(self.metric, ValidationMetricEnum):
            self.metric = ValidationMetricEnum(self.metric)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self.validation_design is not None and not isinstance(self.validation_design, ValidationDesignEnum):
            self.validation_design = ValidationDesignEnum(self.validation_design)

        if self.unit is not None and not isinstance(self.unit, UcumCode):
            self.unit = UcumCode(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Uncertainty(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Uncertainty"]
    class_class_curie: ClassVar[str] = "expo:Uncertainty"
    class_name: ClassVar[str] = "Uncertainty"
    class_model_uri: ClassVar[URIRef] = EXPO.Uncertainty

    type: Union[str, "UncertaintyTypeEnum"] = None
    value: Optional[float] = None
    lower: Optional[float] = None
    upper: Optional[float] = None
    unit: Optional[Union[str, UcumCode]] = None
    carried_to_participant_level: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, UncertaintyTypeEnum):
            self.type = UncertaintyTypeEnum(self.type)

        if self.value is not None and not isinstance(self.value, float):
            self.value = float(self.value)

        if self.lower is not None and not isinstance(self.lower, float):
            self.lower = float(self.lower)

        if self.upper is not None and not isinstance(self.upper, float):
            self.upper = float(self.upper)

        if self.unit is not None and not isinstance(self.unit, UcumCode):
            self.unit = UcumCode(self.unit)

        if self.carried_to_participant_level is not None and not isinstance(self.carried_to_participant_level, Bool):
            self.carried_to_participant_level = Bool(self.carried_to_participant_level)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Linkage(YAMLRoot):
    """
    How exposure values were assigned to participants.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Linkage"]
    class_class_curie: ClassVar[str] = "expo:Linkage"
    class_name: ClassVar[str] = "Linkage"
    class_model_uri: ClassVar[URIRef] = EXPO.Linkage

    spatial_linkage_unit: Union[str, "SpatialLinkageUnitEnum"] = None
    operation: Union[str, "LinkageOperationEnum"] = None
    aggregation: Union[str, "AggregationEnum"] = None
    centroid_weighting: Optional[Union[str, "CentroidWeightingEnum"]] = None
    centroid_areal_unit: Optional[str] = None
    population_dataset: Optional[str] = None
    buffer_radii_m: Optional[Union[float, list[float]]] = empty_list()
    network_mode: Optional[Union[str, "NetworkModeEnum"]] = None
    network_distance_m: Optional[float] = None
    network_time_min: Optional[float] = None
    intersection_min_overlap_pct: Optional[float] = None
    kernel_bandwidth_m: Optional[float] = None
    kernel_grid_resolution_m: Optional[float] = None
    geocoding_precision: Optional[Union[str, "GeocodingPrecisionEnum"]] = None
    geocoding_mixed_breakdown: Optional[str] = None
    geocoder: Optional[str] = None
    aggregation_n: Optional[int] = None
    participant_coverage_pct: Optional[float] = None
    coverage_unit: Optional[Union[str, "CoverageUnitEnum"]] = None
    study_area_coverage_pct: Optional[float] = None
    exposure_window: Optional[Union[str, "ExposureWindowEnum"]] = None
    exposure_window_years: Optional[int] = None
    exposure_window_detail: Optional[str] = None
    residential_history: Optional[Union[str, "ResidentialHistoryEnum"]] = None
    residential_history_detail: Optional[str] = None
    linkage_date: Optional[Union[str, XSDDate]] = None
    relinkages: Optional[Union[Union[dict, "Relinkage"], list[Union[dict, "Relinkage"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.spatial_linkage_unit):
            self.MissingRequiredField("spatial_linkage_unit")
        if not isinstance(self.spatial_linkage_unit, SpatialLinkageUnitEnum):
            self.spatial_linkage_unit = SpatialLinkageUnitEnum(self.spatial_linkage_unit)

        if self._is_empty(self.operation):
            self.MissingRequiredField("operation")
        if not isinstance(self.operation, LinkageOperationEnum):
            self.operation = LinkageOperationEnum(self.operation)

        if self._is_empty(self.aggregation):
            self.MissingRequiredField("aggregation")
        if not isinstance(self.aggregation, AggregationEnum):
            self.aggregation = AggregationEnum(self.aggregation)

        if self.centroid_weighting is not None and not isinstance(self.centroid_weighting, CentroidWeightingEnum):
            self.centroid_weighting = CentroidWeightingEnum(self.centroid_weighting)

        if self.centroid_areal_unit is not None and not isinstance(self.centroid_areal_unit, str):
            self.centroid_areal_unit = str(self.centroid_areal_unit)

        if self.population_dataset is not None and not isinstance(self.population_dataset, str):
            self.population_dataset = str(self.population_dataset)

        if not isinstance(self.buffer_radii_m, list):
            self.buffer_radii_m = [self.buffer_radii_m] if self.buffer_radii_m is not None else []
        self.buffer_radii_m = [v if isinstance(v, float) else float(v) for v in self.buffer_radii_m]

        if self.network_mode is not None and not isinstance(self.network_mode, NetworkModeEnum):
            self.network_mode = NetworkModeEnum(self.network_mode)

        if self.network_distance_m is not None and not isinstance(self.network_distance_m, float):
            self.network_distance_m = float(self.network_distance_m)

        if self.network_time_min is not None and not isinstance(self.network_time_min, float):
            self.network_time_min = float(self.network_time_min)

        if self.intersection_min_overlap_pct is not None and not isinstance(self.intersection_min_overlap_pct, float):
            self.intersection_min_overlap_pct = float(self.intersection_min_overlap_pct)

        if self.kernel_bandwidth_m is not None and not isinstance(self.kernel_bandwidth_m, float):
            self.kernel_bandwidth_m = float(self.kernel_bandwidth_m)

        if self.kernel_grid_resolution_m is not None and not isinstance(self.kernel_grid_resolution_m, float):
            self.kernel_grid_resolution_m = float(self.kernel_grid_resolution_m)

        if self.geocoding_precision is not None and not isinstance(self.geocoding_precision, GeocodingPrecisionEnum):
            self.geocoding_precision = GeocodingPrecisionEnum(self.geocoding_precision)

        if self.geocoding_mixed_breakdown is not None and not isinstance(self.geocoding_mixed_breakdown, str):
            self.geocoding_mixed_breakdown = str(self.geocoding_mixed_breakdown)

        if self.geocoder is not None and not isinstance(self.geocoder, str):
            self.geocoder = str(self.geocoder)

        if self.aggregation_n is not None and not isinstance(self.aggregation_n, int):
            self.aggregation_n = int(self.aggregation_n)

        if self.participant_coverage_pct is not None and not isinstance(self.participant_coverage_pct, float):
            self.participant_coverage_pct = float(self.participant_coverage_pct)

        if self.coverage_unit is not None and not isinstance(self.coverage_unit, CoverageUnitEnum):
            self.coverage_unit = CoverageUnitEnum(self.coverage_unit)

        if self.study_area_coverage_pct is not None and not isinstance(self.study_area_coverage_pct, float):
            self.study_area_coverage_pct = float(self.study_area_coverage_pct)

        if self.exposure_window is not None and not isinstance(self.exposure_window, ExposureWindowEnum):
            self.exposure_window = ExposureWindowEnum(self.exposure_window)

        if self.exposure_window_years is not None and not isinstance(self.exposure_window_years, int):
            self.exposure_window_years = int(self.exposure_window_years)

        if self.exposure_window_detail is not None and not isinstance(self.exposure_window_detail, str):
            self.exposure_window_detail = str(self.exposure_window_detail)

        if self.residential_history is not None and not isinstance(self.residential_history, ResidentialHistoryEnum):
            self.residential_history = ResidentialHistoryEnum(self.residential_history)

        if self.residential_history_detail is not None and not isinstance(self.residential_history_detail, str):
            self.residential_history_detail = str(self.residential_history_detail)

        if self.linkage_date is not None and not isinstance(self.linkage_date, XSDDate):
            self.linkage_date = XSDDate(self.linkage_date)

        self._normalize_inlined_as_list(slot_name="relinkages", slot_type=Relinkage, key_name="date", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relinkage(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Relinkage"]
    class_class_curie: ClassVar[str] = "expo:Relinkage"
    class_name: ClassVar[str] = "Relinkage"
    class_model_uri: ClassVar[URIRef] = EXPO.Relinkage

    date: Union[str, XSDDate] = None
    reason: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        if self._is_empty(self.reason):
            self.MissingRequiredField("reason")
        if not isinstance(self.reason, str):
            self.reason = str(self.reason)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    CSV: Creator(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPO["Person"]
    class_class_curie: ClassVar[str] = "expo:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EXPO.Person

    name: Optional[str] = None
    email: Optional[str] = None
    orcid: Optional[Union[str, CURIE]] = None
    role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.orcid is not None and not isinstance(self.orcid, CURIE):
            self.orcid = CURIE(self.orcid)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        super().__post_init__(**kwargs)


# Enumerations
class CountryCodeEnum(EnumDefinitionImpl):
    """
    ISO 3166-1 alpha-2, officially assigned codes (GB, not UK).
    """
    AD = PermissibleValue(text="AD")
    AE = PermissibleValue(text="AE")
    AF = PermissibleValue(text="AF")
    AG = PermissibleValue(text="AG")
    AI = PermissibleValue(text="AI")
    AL = PermissibleValue(text="AL")
    AM = PermissibleValue(text="AM")
    AO = PermissibleValue(text="AO")
    AQ = PermissibleValue(text="AQ")
    AR = PermissibleValue(text="AR")
    AS = PermissibleValue(text="AS")
    AT = PermissibleValue(text="AT")
    AU = PermissibleValue(text="AU")
    AW = PermissibleValue(text="AW")
    AX = PermissibleValue(text="AX")
    AZ = PermissibleValue(text="AZ")
    BA = PermissibleValue(text="BA")
    BB = PermissibleValue(text="BB")
    BD = PermissibleValue(text="BD")
    BE = PermissibleValue(text="BE")
    BF = PermissibleValue(text="BF")
    BG = PermissibleValue(text="BG")
    BH = PermissibleValue(text="BH")
    BI = PermissibleValue(text="BI")
    BJ = PermissibleValue(text="BJ")
    BL = PermissibleValue(text="BL")
    BM = PermissibleValue(text="BM")
    BN = PermissibleValue(text="BN")
    BO = PermissibleValue(text="BO")
    BQ = PermissibleValue(text="BQ")
    BR = PermissibleValue(text="BR")
    BS = PermissibleValue(text="BS")
    BT = PermissibleValue(text="BT")
    BV = PermissibleValue(text="BV")
    BW = PermissibleValue(text="BW")
    BY = PermissibleValue(text="BY")
    BZ = PermissibleValue(text="BZ")
    CA = PermissibleValue(text="CA")
    CC = PermissibleValue(text="CC")
    CD = PermissibleValue(text="CD")
    CF = PermissibleValue(text="CF")
    CG = PermissibleValue(text="CG")
    CH = PermissibleValue(text="CH")
    CI = PermissibleValue(text="CI")
    CK = PermissibleValue(text="CK")
    CL = PermissibleValue(text="CL")
    CM = PermissibleValue(text="CM")
    CN = PermissibleValue(text="CN")
    CO = PermissibleValue(text="CO")
    CR = PermissibleValue(text="CR")
    CU = PermissibleValue(text="CU")
    CV = PermissibleValue(text="CV")
    CW = PermissibleValue(text="CW")
    CX = PermissibleValue(text="CX")
    CY = PermissibleValue(text="CY")
    CZ = PermissibleValue(text="CZ")
    DE = PermissibleValue(text="DE")
    DJ = PermissibleValue(text="DJ")
    DK = PermissibleValue(text="DK")
    DM = PermissibleValue(text="DM")
    DO = PermissibleValue(text="DO")
    DZ = PermissibleValue(text="DZ")
    EC = PermissibleValue(text="EC")
    EE = PermissibleValue(text="EE")
    EG = PermissibleValue(text="EG")
    EH = PermissibleValue(text="EH")
    ER = PermissibleValue(text="ER")
    ES = PermissibleValue(text="ES")
    ET = PermissibleValue(text="ET")
    FI = PermissibleValue(text="FI")
    FJ = PermissibleValue(text="FJ")
    FK = PermissibleValue(text="FK")
    FM = PermissibleValue(text="FM")
    FO = PermissibleValue(text="FO")
    FR = PermissibleValue(text="FR")
    GA = PermissibleValue(text="GA")
    GB = PermissibleValue(text="GB")
    GD = PermissibleValue(text="GD")
    GE = PermissibleValue(text="GE")
    GF = PermissibleValue(text="GF")
    GG = PermissibleValue(text="GG")
    GH = PermissibleValue(text="GH")
    GI = PermissibleValue(text="GI")
    GL = PermissibleValue(text="GL")
    GM = PermissibleValue(text="GM")
    GN = PermissibleValue(text="GN")
    GP = PermissibleValue(text="GP")
    GQ = PermissibleValue(text="GQ")
    GR = PermissibleValue(text="GR")
    GS = PermissibleValue(text="GS")
    GT = PermissibleValue(text="GT")
    GU = PermissibleValue(text="GU")
    GW = PermissibleValue(text="GW")
    GY = PermissibleValue(text="GY")
    HK = PermissibleValue(text="HK")
    HM = PermissibleValue(text="HM")
    HN = PermissibleValue(text="HN")
    HR = PermissibleValue(text="HR")
    HT = PermissibleValue(text="HT")
    HU = PermissibleValue(text="HU")
    ID = PermissibleValue(text="ID")
    IE = PermissibleValue(text="IE")
    IL = PermissibleValue(text="IL")
    IM = PermissibleValue(text="IM")
    IN = PermissibleValue(text="IN")
    IO = PermissibleValue(text="IO")
    IQ = PermissibleValue(text="IQ")
    IR = PermissibleValue(text="IR")
    IS = PermissibleValue(text="IS")
    IT = PermissibleValue(text="IT")
    JE = PermissibleValue(text="JE")
    JM = PermissibleValue(text="JM")
    JO = PermissibleValue(text="JO")
    JP = PermissibleValue(text="JP")
    KE = PermissibleValue(text="KE")
    KG = PermissibleValue(text="KG")
    KH = PermissibleValue(text="KH")
    KI = PermissibleValue(text="KI")
    KM = PermissibleValue(text="KM")
    KN = PermissibleValue(text="KN")
    KP = PermissibleValue(text="KP")
    KR = PermissibleValue(text="KR")
    KW = PermissibleValue(text="KW")
    KY = PermissibleValue(text="KY")
    KZ = PermissibleValue(text="KZ")
    LA = PermissibleValue(text="LA")
    LB = PermissibleValue(text="LB")
    LC = PermissibleValue(text="LC")
    LI = PermissibleValue(text="LI")
    LK = PermissibleValue(text="LK")
    LR = PermissibleValue(text="LR")
    LS = PermissibleValue(text="LS")
    LT = PermissibleValue(text="LT")
    LU = PermissibleValue(text="LU")
    LV = PermissibleValue(text="LV")
    LY = PermissibleValue(text="LY")
    MA = PermissibleValue(text="MA")
    MC = PermissibleValue(text="MC")
    MD = PermissibleValue(text="MD")
    ME = PermissibleValue(text="ME")
    MF = PermissibleValue(text="MF")
    MG = PermissibleValue(text="MG")
    MH = PermissibleValue(text="MH")
    MK = PermissibleValue(text="MK")
    ML = PermissibleValue(text="ML")
    MM = PermissibleValue(text="MM")
    MN = PermissibleValue(text="MN")
    MO = PermissibleValue(text="MO")
    MP = PermissibleValue(text="MP")
    MQ = PermissibleValue(text="MQ")
    MR = PermissibleValue(text="MR")
    MS = PermissibleValue(text="MS")
    MT = PermissibleValue(text="MT")
    MU = PermissibleValue(text="MU")
    MV = PermissibleValue(text="MV")
    MW = PermissibleValue(text="MW")
    MX = PermissibleValue(text="MX")
    MY = PermissibleValue(text="MY")
    MZ = PermissibleValue(text="MZ")
    NA = PermissibleValue(text="NA")
    NC = PermissibleValue(text="NC")
    NE = PermissibleValue(text="NE")
    NF = PermissibleValue(text="NF")
    NG = PermissibleValue(text="NG")
    NI = PermissibleValue(text="NI")
    NL = PermissibleValue(text="NL")
    NO = PermissibleValue(text="NO")
    NP = PermissibleValue(text="NP")
    NR = PermissibleValue(text="NR")
    NU = PermissibleValue(text="NU")
    NZ = PermissibleValue(text="NZ")
    OM = PermissibleValue(text="OM")
    PA = PermissibleValue(text="PA")
    PE = PermissibleValue(text="PE")
    PF = PermissibleValue(text="PF")
    PG = PermissibleValue(text="PG")
    PH = PermissibleValue(text="PH")
    PK = PermissibleValue(text="PK")
    PL = PermissibleValue(text="PL")
    PM = PermissibleValue(text="PM")
    PN = PermissibleValue(text="PN")
    PR = PermissibleValue(text="PR")
    PS = PermissibleValue(text="PS")
    PT = PermissibleValue(text="PT")
    PW = PermissibleValue(text="PW")
    PY = PermissibleValue(text="PY")
    QA = PermissibleValue(text="QA")
    RE = PermissibleValue(text="RE")
    RO = PermissibleValue(text="RO")
    RS = PermissibleValue(text="RS")
    RU = PermissibleValue(text="RU")
    RW = PermissibleValue(text="RW")
    SA = PermissibleValue(text="SA")
    SB = PermissibleValue(text="SB")
    SC = PermissibleValue(text="SC")
    SD = PermissibleValue(text="SD")
    SE = PermissibleValue(text="SE")
    SG = PermissibleValue(text="SG")
    SH = PermissibleValue(text="SH")
    SI = PermissibleValue(text="SI")
    SJ = PermissibleValue(text="SJ")
    SK = PermissibleValue(text="SK")
    SL = PermissibleValue(text="SL")
    SM = PermissibleValue(text="SM")
    SN = PermissibleValue(text="SN")
    SO = PermissibleValue(text="SO")
    SR = PermissibleValue(text="SR")
    SS = PermissibleValue(text="SS")
    ST = PermissibleValue(text="ST")
    SV = PermissibleValue(text="SV")
    SX = PermissibleValue(text="SX")
    SY = PermissibleValue(text="SY")
    SZ = PermissibleValue(text="SZ")
    TC = PermissibleValue(text="TC")
    TD = PermissibleValue(text="TD")
    TF = PermissibleValue(text="TF")
    TG = PermissibleValue(text="TG")
    TH = PermissibleValue(text="TH")
    TJ = PermissibleValue(text="TJ")
    TK = PermissibleValue(text="TK")
    TL = PermissibleValue(text="TL")
    TM = PermissibleValue(text="TM")
    TN = PermissibleValue(text="TN")
    TO = PermissibleValue(text="TO")
    TR = PermissibleValue(text="TR")
    TT = PermissibleValue(text="TT")
    TV = PermissibleValue(text="TV")
    TW = PermissibleValue(text="TW")
    TZ = PermissibleValue(text="TZ")
    UA = PermissibleValue(text="UA")
    UG = PermissibleValue(text="UG")
    UM = PermissibleValue(text="UM")
    US = PermissibleValue(text="US")
    UY = PermissibleValue(text="UY")
    UZ = PermissibleValue(text="UZ")
    VA = PermissibleValue(text="VA")
    VC = PermissibleValue(text="VC")
    VE = PermissibleValue(text="VE")
    VG = PermissibleValue(text="VG")
    VI = PermissibleValue(text="VI")
    VN = PermissibleValue(text="VN")
    VU = PermissibleValue(text="VU")
    WF = PermissibleValue(text="WF")
    WS = PermissibleValue(text="WS")
    YE = PermissibleValue(text="YE")
    YT = PermissibleValue(text="YT")
    ZA = PermissibleValue(text="ZA")
    ZM = PermissibleValue(text="ZM")
    ZW = PermissibleValue(text="ZW")

    _defn = EnumDefinition(
        name="CountryCodeEnum",
        description="ISO 3166-1 alpha-2, officially assigned codes (GB, not UK).",
    )

class ExposureDomainEnum(EnumDefinitionImpl):

    AIR_POLLUTION = PermissibleValue(text="AIR_POLLUTION")
    CLIMATE_WEATHER = PermissibleValue(text="CLIMATE_WEATHER")
    GREEN_SPACE = PermissibleValue(text="GREEN_SPACE")
    BLUE_SPACE = PermissibleValue(text="BLUE_SPACE")
    NOISE = PermissibleValue(text="NOISE")
    SOCIODEMOGRAPHIC = PermissibleValue(text="SOCIODEMOGRAPHIC")
    BUILT_ENVIRONMENT = PermissibleValue(text="BUILT_ENVIRONMENT")
    WATER_QUALITY = PermissibleValue(text="WATER_QUALITY")
    LIGHT_POLLUTION = PermissibleValue(text="LIGHT_POLLUTION")
    BIODIVERSITY = PermissibleValue(text="BIODIVERSITY")
    INDOOR_HOME_ENVIRONMENT = PermissibleValue(text="INDOOR_HOME_ENVIRONMENT")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="ExposureDomainEnum",
    )

class DataOriginEnum(EnumDefinitionImpl):

    MONITORING_STATION = PermissibleValue(text="MONITORING_STATION")
    LAND_USE_REGRESSION = PermissibleValue(text="LAND_USE_REGRESSION")
    CHEMICAL_TRANSPORT_MODEL = PermissibleValue(text="CHEMICAL_TRANSPORT_MODEL")
    SATELLITE_DERIVED = PermissibleValue(text="SATELLITE_DERIVED")
    PERSONAL_MONITOR = PermissibleValue(text="PERSONAL_MONITOR")
    QUESTIONNAIRE = PermissibleValue(text="QUESTIONNAIRE")
    ADMINISTRATIVE_RECORD = PermissibleValue(text="ADMINISTRATIVE_RECORD")
    REANALYSIS = PermissibleValue(
        text="REANALYSIS",
        description="Added - ERA5-type products were otherwise unclassifiable.")
    OTHER = PermissibleValue(text="OTHER")

    _defn = EnumDefinition(
        name="DataOriginEnum",
    )

class GeographicScopeEnum(EnumDefinitionImpl):

    COUNTRIES_OR_REGIONS = PermissibleValue(text="COUNTRIES_OR_REGIONS")
    EU27 = PermissibleValue(text="EU27")
    GLOBAL = PermissibleValue(text="GLOBAL")

    _defn = EnumDefinition(
        name="GeographicScopeEnum",
    )

class SpatialResolutionTypeEnum(EnumDefinitionImpl):

    GRID_METRIC = PermissibleValue(text="GRID_METRIC")
    GRID_DEGREE = PermissibleValue(text="GRID_DEGREE")
    ADMINISTRATIVE_UNIT = PermissibleValue(text="ADMINISTRATIVE_UNIT")
    POINT_ADDRESS = PermissibleValue(text="POINT_ADDRESS")
    POINT_GPS = PermissibleValue(text="POINT_GPS")

    _defn = EnumDefinition(
        name="SpatialResolutionTypeEnum",
    )

class TemporalResolutionEnum(EnumDefinitionImpl):

    SUB_HOURLY = PermissibleValue(text="SUB_HOURLY")
    HOURLY = PermissibleValue(text="HOURLY")
    DAILY = PermissibleValue(text="DAILY")
    WEEKLY = PermissibleValue(text="WEEKLY")
    MONTHLY = PermissibleValue(text="MONTHLY")
    SEASONAL = PermissibleValue(text="SEASONAL")
    ANNUAL = PermissibleValue(text="ANNUAL")
    MULTI_YEAR_AVERAGE = PermissibleValue(text="MULTI_YEAR_AVERAGE")
    EVENT_BASED = PermissibleValue(text="EVENT_BASED")
    STATIC = PermissibleValue(text="STATIC")
    PERIODIC_UPDATE = PermissibleValue(text="PERIODIC_UPDATE")

    _defn = EnumDefinition(
        name="TemporalResolutionEnum",
    )

class ValidationMetricEnum(EnumDefinitionImpl):

    R2 = PermissibleValue(text="R2")
    RMSE = PermissibleValue(text="RMSE")
    NRMSE_PCT = PermissibleValue(text="NRMSE_PCT")
    MEAN_BIAS = PermissibleValue(text="MEAN_BIAS")
    RELATIVE_BIAS_PCT = PermissibleValue(text="RELATIVE_BIAS_PCT")
    PEARSON_R = PermissibleValue(text="PEARSON_R")

    _defn = EnumDefinition(
        name="ValidationMetricEnum",
    )

class ValidationDesignEnum(EnumDefinitionImpl):

    LOOCV_SPATIAL = PermissibleValue(text="LOOCV_SPATIAL")
    INDEPENDENT_TEST_SET_SPATIAL = PermissibleValue(text="INDEPENDENT_TEST_SET_SPATIAL")
    TEMPORAL = PermissibleValue(text="TEMPORAL")
    OVERALL = PermissibleValue(text="OVERALL")
    GROUND_MONITOR_COMPARISON = PermissibleValue(text="GROUND_MONITOR_COMPARISON")

    _defn = EnumDefinition(
        name="ValidationDesignEnum",
    )

class UncertaintyTypeEnum(EnumDefinitionImpl):

    NOT_AVAILABLE = PermissibleValue(text="NOT_AVAILABLE")
    SD_PER_UNIT = PermissibleValue(text="SD_PER_UNIT")
    PREDICTION_INTERVAL_95 = PermissibleValue(text="PREDICTION_INTERVAL_95")
    FULL_PREDICTIVE_DISTRIBUTION = PermissibleValue(text="FULL_PREDICTIVE_DISTRIBUTION")
    MODEL_LEVEL_RMSE_ONLY = PermissibleValue(text="MODEL_LEVEL_RMSE_ONLY")

    _defn = EnumDefinition(
        name="UncertaintyTypeEnum",
    )

class SpatialLinkageUnitEnum(EnumDefinitionImpl):

    GEOCODED_ADDRESS = PermissibleValue(text="GEOCODED_ADDRESS")
    GPS_COORDINATE = PermissibleValue(text="GPS_COORDINATE")
    POSTCODE_CENTROID = PermissibleValue(text="POSTCODE_CENTROID")
    CENSUS_TRACT_CENTROID = PermissibleValue(text="CENSUS_TRACT_CENTROID")
    LSOA_CENTROID = PermissibleValue(text="LSOA_CENTROID")
    MUNICIPALITY_CENTROID = PermissibleValue(text="MUNICIPALITY_CENTROID")
    OTHER_AREAL_CENTROID = PermissibleValue(text="OTHER_AREAL_CENTROID")
    GRID_CELL_CONTAINING_ADDRESS = PermissibleValue(text="GRID_CELL_CONTAINING_ADDRESS")

    _defn = EnumDefinition(
        name="SpatialLinkageUnitEnum",
    )

class CentroidWeightingEnum(EnumDefinitionImpl):

    GEOMETRIC = PermissibleValue(text="GEOMETRIC")
    POPULATION_WEIGHTED = PermissibleValue(text="POPULATION_WEIGHTED")
    AREA_WEIGHTED = PermissibleValue(text="AREA_WEIGHTED")

    _defn = EnumDefinition(
        name="CentroidWeightingEnum",
    )

class LinkageOperationEnum(EnumDefinitionImpl):

    POINT_IN_POLYGON = PermissibleValue(text="POINT_IN_POLYGON")
    CIRCULAR_BUFFER = PermissibleValue(text="CIRCULAR_BUFFER")
    NETWORK_BUFFER = PermissibleValue(text="NETWORK_BUFFER")
    NEAREST_FEATURE = PermissibleValue(text="NEAREST_FEATURE")
    AREAL_INTERPOLATION = PermissibleValue(text="AREAL_INTERPOLATION")
    INTERSECTION = PermissibleValue(text="INTERSECTION")
    KERNEL_DENSITY_WEIGHTED = PermissibleValue(text="KERNEL_DENSITY_WEIGHTED")
    ADMINISTRATIVE_ASSIGNMENT = PermissibleValue(text="ADMINISTRATIVE_ASSIGNMENT")

    _defn = EnumDefinition(
        name="LinkageOperationEnum",
    )

class NetworkModeEnum(EnumDefinitionImpl):

    WALKING = PermissibleValue(text="WALKING")
    CYCLING = PermissibleValue(text="CYCLING")
    DRIVING = PermissibleValue(text="DRIVING")
    PUBLIC_TRANSPORT = PermissibleValue(text="PUBLIC_TRANSPORT")

    _defn = EnumDefinition(
        name="NetworkModeEnum",
    )

class GeocodingPrecisionEnum(EnumDefinitionImpl):

    BUILDING = PermissibleValue(
        text="BUILDING",
        description="< 5 m")
    PARCEL = PermissibleValue(
        text="PARCEL",
        description="< 10 m")
    STREET = PermissibleValue(
        text="STREET",
        description="< 50 m")
    POSTCODE_CENTROID = PermissibleValue(
        text="POSTCODE_CENTROID",
        description="< 500 m")
    CENSUS_UNIT_CENTROID = PermissibleValue(
        text="CENSUS_UNIT_CENTROID",
        description="> 500 m")
    MIXED = PermissibleValue(text="MIXED")
    UNKNOWN = PermissibleValue(text="UNKNOWN")

    _defn = EnumDefinition(
        name="GeocodingPrecisionEnum",
    )

class AggregationEnum(EnumDefinitionImpl):

    ANNUAL_MEAN = PermissibleValue(text="ANNUAL_MEAN")
    MONTHLY_MEAN = PermissibleValue(text="MONTHLY_MEAN")
    DAILY_MEAN = PermissibleValue(text="DAILY_MEAN")
    DAILY_MAX = PermissibleValue(text="DAILY_MAX")
    DAILY_MIN = PermissibleValue(text="DAILY_MIN")
    EIGHT_HOUR_MEAN = PermissibleValue(text="EIGHT_HOUR_MEAN")
    WARM_SEASON_MEAN = PermissibleValue(text="WARM_SEASON_MEAN")
    COLD_SEASON_MEAN = PermissibleValue(text="COLD_SEASON_MEAN")
    NIGHT_TIME_MEAN = PermissibleValue(text="NIGHT_TIME_MEAN")
    MULTI_YEAR_MEAN = PermissibleValue(text="MULTI_YEAR_MEAN")
    CUMULATIVE_SUM = PermissibleValue(text="CUMULATIVE_SUM")
    PERCENTILE = PermissibleValue(text="PERCENTILE")
    PRESENCE_ABSENCE = PermissibleValue(text="PRESENCE_ABSENCE")
    DISTANCE_TO_NEAREST = PermissibleValue(text="DISTANCE_TO_NEAREST")
    COUNT_WITHIN_BUFFER = PermissibleValue(text="COUNT_WITHIN_BUFFER")
    MEAN_WITHIN_BUFFER = PermissibleValue(
        text="MEAN_WITHIN_BUFFER",
        description="Buffer geometry lives in linkage.operation - not duplicated here.")
    COMPOSITE_INDEX = PermissibleValue(text="COMPOSITE_INDEX")
    RAW_TIME_SERIES = PermissibleValue(text="RAW_TIME_SERIES")

    _defn = EnumDefinition(
        name="AggregationEnum",
    )

class CoverageUnitEnum(EnumDefinitionImpl):

    PARTICIPANTS = PermissibleValue(text="PARTICIPANTS")
    HOUSEHOLDS = PermissibleValue(text="HOUSEHOLDS")
    CLINICAL_SITES = PermissibleValue(text="CLINICAL_SITES")
    HOSPITALS = PermissibleValue(text="HOSPITALS")
    GEOGRAPHIC_UNITS = PermissibleValue(text="GEOGRAPHIC_UNITS")

    _defn = EnumDefinition(
        name="CoverageUnitEnum",
    )

class ExposureWindowEnum(EnumDefinitionImpl):

    YEAR_BEFORE_RECRUITMENT = PermissibleValue(text="YEAR_BEFORE_RECRUITMENT")
    N_YEARS_BEFORE_INDEX = PermissibleValue(text="N_YEARS_BEFORE_INDEX")
    PRENATAL = PermissibleValue(text="PRENATAL")
    PERICONCEPTION = PermissibleValue(text="PERICONCEPTION")
    INFANCY = PermissibleValue(text="INFANCY")
    EARLY_CHILDHOOD = PermissibleValue(text="EARLY_CHILDHOOD")
    ADOLESCENCE = PermissibleValue(text="ADOLESCENCE")
    LIFETIME_CUMULATIVE = PermissibleValue(text="LIFETIME_CUMULATIVE")
    TIME_VARYING_ANNUAL = PermissibleValue(text="TIME_VARYING_ANNUAL")
    CRITICAL_WINDOW = PermissibleValue(text="CRITICAL_WINDOW")

    _defn = EnumDefinition(
        name="ExposureWindowEnum",
    )

class ResidentialHistoryEnum(EnumDefinitionImpl):

    BASELINE_ONLY = PermissibleValue(text="BASELINE_ONLY")
    FULL_HISTORY = PermissibleValue(text="FULL_HISTORY")
    PARTIAL_HISTORY = PermissibleValue(text="PARTIAL_HISTORY")
    NOT_APPLICABLE = PermissibleValue(text="NOT_APPLICABLE")
    UNKNOWN = PermissibleValue(text="UNKNOWN")

    _defn = EnumDefinition(
        name="ResidentialHistoryEnum",
    )

# Slots
class slots:
    pass

slots.exposureLinkageCollection__records = Slot(uri=EXPO.records, name="exposureLinkageCollection__records", curie=EXPO.curie('records'),
                   model_uri=EXPO.exposureLinkageCollection__records, domain=None, range=Union[dict[Union[str, ExposureLinkageRecordId], Union[dict, ExposureLinkageRecord]], list[Union[dict, ExposureLinkageRecord]]])

slots.exposureLinkageRecord__id = Slot(uri=EXPO.id, name="exposureLinkageRecord__id", curie=EXPO.curie('id'),
                   model_uri=EXPO.exposureLinkageRecord__id, domain=None, range=URIRef)

slots.exposureLinkageRecord__cohort = Slot(uri=EXPO.cohort, name="exposureLinkageRecord__cohort", curie=EXPO.curie('cohort'),
                   model_uri=EXPO.exposureLinkageRecord__cohort, domain=None, range=Union[dict, Cohort])

slots.exposureLinkageRecord__exposure = Slot(uri=EXPO.exposure, name="exposureLinkageRecord__exposure", curie=EXPO.curie('exposure'),
                   model_uri=EXPO.exposureLinkageRecord__exposure, domain=None, range=Union[dict, ExposureVariable])

slots.exposureLinkageRecord__source_data = Slot(uri=EXPO.source_data, name="exposureLinkageRecord__source_data", curie=EXPO.curie('source_data'),
                   model_uri=EXPO.exposureLinkageRecord__source_data, domain=None, range=Union[dict, SourceDataset])

slots.exposureLinkageRecord__linkage = Slot(uri=EXPO.linkage, name="exposureLinkageRecord__linkage", curie=EXPO.curie('linkage'),
                   model_uri=EXPO.exposureLinkageRecord__linkage, domain=None, range=Union[dict, Linkage])

slots.exposureLinkageRecord__creators = Slot(uri=EXPO.creators, name="exposureLinkageRecord__creators", curie=EXPO.curie('creators'),
                   model_uri=EXPO.exposureLinkageRecord__creators, domain=None, range=Optional[Union[Union[dict, Person], list[Union[dict, Person]]]])

slots.cohort__name = Slot(uri=EXPO.name, name="cohort__name", curie=EXPO.curie('name'),
                   model_uri=EXPO.cohort__name, domain=None, range=str)

slots.cohort__acronym = Slot(uri=EXPO.acronym, name="cohort__acronym", curie=EXPO.curie('acronym'),
                   model_uri=EXPO.cohort__acronym, domain=None, range=str)

slots.cohort__collection_countries = Slot(uri=EXPO.collection_countries, name="cohort__collection_countries", curie=EXPO.curie('collection_countries'),
                   model_uri=EXPO.cohort__collection_countries, domain=None, range=Union[Union[str, "CountryCodeEnum"], list[Union[str, "CountryCodeEnum"]]])

slots.exposureVariable__domain = Slot(uri=EXPO.domain, name="exposureVariable__domain", curie=EXPO.curie('domain'),
                   model_uri=EXPO.exposureVariable__domain, domain=None, range=Union[str, "ExposureDomainEnum"])

slots.exposureVariable__domain_other = Slot(uri=EXPO.domain_other, name="exposureVariable__domain_other", curie=EXPO.curie('domain_other'),
                   model_uri=EXPO.exposureVariable__domain_other, domain=None, range=Optional[str])

slots.exposureVariable__name = Slot(uri=EXPO.name, name="exposureVariable__name", curie=EXPO.curie('name'),
                   model_uri=EXPO.exposureVariable__name, domain=None, range=str)

slots.exposureVariable__ontology_terms = Slot(uri=EXPO.ontology_terms, name="exposureVariable__ontology_terms", curie=EXPO.curie('ontology_terms'),
                   model_uri=EXPO.exposureVariable__ontology_terms, domain=None, range=Optional[Union[Union[str, CURIE], list[Union[str, CURIE]]]])

slots.exposureVariable__unit = Slot(uri=EXPO.unit, name="exposureVariable__unit", curie=EXPO.curie('unit'),
                   model_uri=EXPO.exposureVariable__unit, domain=None, range=Optional[Union[str, UcumCode]])

slots.exposureVariable__is_categorical = Slot(uri=EXPO.is_categorical, name="exposureVariable__is_categorical", curie=EXPO.curie('is_categorical'),
                   model_uri=EXPO.exposureVariable__is_categorical, domain=None, range=Optional[Union[bool, Bool]])

slots.sourceDataset__origin = Slot(uri=EXPO.origin, name="sourceDataset__origin", curie=EXPO.curie('origin'),
                   model_uri=EXPO.sourceDataset__origin, domain=None, range=Union[str, "DataOriginEnum"])

slots.sourceDataset__dataset_name = Slot(uri=EXPO.dataset_name, name="sourceDataset__dataset_name", curie=EXPO.curie('dataset_name'),
                   model_uri=EXPO.sourceDataset__dataset_name, domain=None, range=str)

slots.sourceDataset__dataset_version = Slot(uri=EXPO.dataset_version, name="sourceDataset__dataset_version", curie=EXPO.curie('dataset_version'),
                   model_uri=EXPO.sourceDataset__dataset_version, domain=None, range=str)

slots.sourceDataset__citations = Slot(uri=EXPO.citations, name="sourceDataset__citations", curie=EXPO.curie('citations'),
                   model_uri=EXPO.sourceDataset__citations, domain=None, range=Union[Union[dict, Citation], list[Union[dict, Citation]]])

slots.sourceDataset__geographic_coverage = Slot(uri=EXPO.geographic_coverage, name="sourceDataset__geographic_coverage", curie=EXPO.curie('geographic_coverage'),
                   model_uri=EXPO.sourceDataset__geographic_coverage, domain=None, range=Union[dict, GeographicCoverage])

slots.sourceDataset__spatial_resolution = Slot(uri=EXPO.spatial_resolution, name="sourceDataset__spatial_resolution", curie=EXPO.curie('spatial_resolution'),
                   model_uri=EXPO.sourceDataset__spatial_resolution, domain=None, range=Union[dict, SpatialResolution])

slots.sourceDataset__temporal_coverage = Slot(uri=EXPO.temporal_coverage, name="sourceDataset__temporal_coverage", curie=EXPO.curie('temporal_coverage'),
                   model_uri=EXPO.sourceDataset__temporal_coverage, domain=None, range=Union[dict, TemporalCoverage])

slots.sourceDataset__temporal_resolution = Slot(uri=EXPO.temporal_resolution, name="sourceDataset__temporal_resolution", curie=EXPO.curie('temporal_resolution'),
                   model_uri=EXPO.sourceDataset__temporal_resolution, domain=None, range=Union[str, "TemporalResolutionEnum"])

slots.sourceDataset__update_frequency = Slot(uri=EXPO.update_frequency, name="sourceDataset__update_frequency", curie=EXPO.curie('update_frequency'),
                   model_uri=EXPO.sourceDataset__update_frequency, domain=None, range=Optional[str],
                   pattern=re.compile(r'^P(\d+Y)?(\d+M)?(\d+W)?(\d+D)?$'))

slots.sourceDataset__validation_metrics = Slot(uri=EXPO.validation_metrics, name="sourceDataset__validation_metrics", curie=EXPO.curie('validation_metrics'),
                   model_uri=EXPO.sourceDataset__validation_metrics, domain=None, range=Optional[Union[Union[dict, ValidationMetric], list[Union[dict, ValidationMetric]]]])

slots.sourceDataset__validation_reported = Slot(uri=EXPO.validation_reported, name="sourceDataset__validation_reported", curie=EXPO.curie('validation_reported'),
                   model_uri=EXPO.sourceDataset__validation_reported, domain=None, range=Optional[Union[bool, Bool]])

slots.sourceDataset__uncertainty = Slot(uri=EXPO.uncertainty, name="sourceDataset__uncertainty", curie=EXPO.curie('uncertainty'),
                   model_uri=EXPO.sourceDataset__uncertainty, domain=None, range=Optional[Union[dict, Uncertainty]])

slots.citation__doi = Slot(uri=EXPO.doi, name="citation__doi", curie=EXPO.curie('doi'),
                   model_uri=EXPO.citation__doi, domain=None, range=Optional[str],
                   pattern=re.compile(r'^10\.\d{4,9}/\S+$'))

slots.citation__url = Slot(uri=EXPO.url, name="citation__url", curie=EXPO.curie('url'),
                   model_uri=EXPO.citation__url, domain=None, range=Optional[Union[str, URI]])

slots.citation__accessed = Slot(uri=EXPO.accessed, name="citation__accessed", curie=EXPO.curie('accessed'),
                   model_uri=EXPO.citation__accessed, domain=None, range=Optional[Union[str, XSDDate]])

slots.citation__text = Slot(uri=EXPO.text, name="citation__text", curie=EXPO.curie('text'),
                   model_uri=EXPO.citation__text, domain=None, range=Optional[str])

slots.citation__used_for_linkage = Slot(uri=EXPO.used_for_linkage, name="citation__used_for_linkage", curie=EXPO.curie('used_for_linkage'),
                   model_uri=EXPO.citation__used_for_linkage, domain=None, range=Optional[Union[bool, Bool]])

slots.geographicCoverage__scope = Slot(uri=EXPO.scope, name="geographicCoverage__scope", curie=EXPO.curie('scope'),
                   model_uri=EXPO.geographicCoverage__scope, domain=None, range=Union[str, "GeographicScopeEnum"])

slots.geographicCoverage__regions = Slot(uri=EXPO.regions, name="geographicCoverage__regions", curie=EXPO.curie('regions'),
                   model_uri=EXPO.geographicCoverage__regions, domain=None, range=Optional[Union[Union[str, RegionCode], list[Union[str, RegionCode]]]])

slots.geographicCoverage__description = Slot(uri=EXPO.description, name="geographicCoverage__description", curie=EXPO.curie('description'),
                   model_uri=EXPO.geographicCoverage__description, domain=None, range=Optional[str])

slots.spatialResolution__type = Slot(uri=EXPO.type, name="spatialResolution__type", curie=EXPO.curie('type'),
                   model_uri=EXPO.spatialResolution__type, domain=None, range=Union[str, "SpatialResolutionTypeEnum"])

slots.spatialResolution__cell_width = Slot(uri=EXPO.cell_width, name="spatialResolution__cell_width", curie=EXPO.curie('cell_width'),
                   model_uri=EXPO.spatialResolution__cell_width, domain=None, range=Optional[float])

slots.spatialResolution__cell_height = Slot(uri=EXPO.cell_height, name="spatialResolution__cell_height", curie=EXPO.curie('cell_height'),
                   model_uri=EXPO.spatialResolution__cell_height, domain=None, range=Optional[float])

slots.spatialResolution__admin_unit_name = Slot(uri=EXPO.admin_unit_name, name="spatialResolution__admin_unit_name", curie=EXPO.curie('admin_unit_name'),
                   model_uri=EXPO.spatialResolution__admin_unit_name, domain=None, range=Optional[str])

slots.spatialResolution__admin_unit_approx_population = Slot(uri=EXPO.admin_unit_approx_population, name="spatialResolution__admin_unit_approx_population", curie=EXPO.curie('admin_unit_approx_population'),
                   model_uri=EXPO.spatialResolution__admin_unit_approx_population, domain=None, range=Optional[int])

slots.temporalCoverage__start = Slot(uri=EXPO.start, name="temporalCoverage__start", curie=EXPO.curie('start'),
                   model_uri=EXPO.temporalCoverage__start, domain=None, range=Union[str, PartialDate])

slots.temporalCoverage__end = Slot(uri=EXPO.end, name="temporalCoverage__end", curie=EXPO.curie('end'),
                   model_uri=EXPO.temporalCoverage__end, domain=None, range=Optional[Union[str, PartialDate]])

slots.temporalCoverage__ongoing = Slot(uri=EXPO.ongoing, name="temporalCoverage__ongoing", curie=EXPO.curie('ongoing'),
                   model_uri=EXPO.temporalCoverage__ongoing, domain=None, range=Optional[Union[bool, Bool]])

slots.temporalCoverage__last_updated = Slot(uri=EXPO.last_updated, name="temporalCoverage__last_updated", curie=EXPO.curie('last_updated'),
                   model_uri=EXPO.temporalCoverage__last_updated, domain=None, range=Optional[Union[str, PartialDate]])

slots.validationMetric__metric = Slot(uri=EXPO.metric, name="validationMetric__metric", curie=EXPO.curie('metric'),
                   model_uri=EXPO.validationMetric__metric, domain=None, range=Union[str, "ValidationMetricEnum"])

slots.validationMetric__validation_design = Slot(uri=EXPO.validation_design, name="validationMetric__validation_design", curie=EXPO.curie('validation_design'),
                   model_uri=EXPO.validationMetric__validation_design, domain=None, range=Optional[Union[str, "ValidationDesignEnum"]])

slots.validationMetric__value = Slot(uri=EXPO.value, name="validationMetric__value", curie=EXPO.curie('value'),
                   model_uri=EXPO.validationMetric__value, domain=None, range=float)

slots.validationMetric__unit = Slot(uri=EXPO.unit, name="validationMetric__unit", curie=EXPO.curie('unit'),
                   model_uri=EXPO.validationMetric__unit, domain=None, range=Optional[Union[str, UcumCode]])

slots.uncertainty__type = Slot(uri=EXPO.type, name="uncertainty__type", curie=EXPO.curie('type'),
                   model_uri=EXPO.uncertainty__type, domain=None, range=Union[str, "UncertaintyTypeEnum"])

slots.uncertainty__value = Slot(uri=EXPO.value, name="uncertainty__value", curie=EXPO.curie('value'),
                   model_uri=EXPO.uncertainty__value, domain=None, range=Optional[float])

slots.uncertainty__lower = Slot(uri=EXPO.lower, name="uncertainty__lower", curie=EXPO.curie('lower'),
                   model_uri=EXPO.uncertainty__lower, domain=None, range=Optional[float])

slots.uncertainty__upper = Slot(uri=EXPO.upper, name="uncertainty__upper", curie=EXPO.curie('upper'),
                   model_uri=EXPO.uncertainty__upper, domain=None, range=Optional[float])

slots.uncertainty__unit = Slot(uri=EXPO.unit, name="uncertainty__unit", curie=EXPO.curie('unit'),
                   model_uri=EXPO.uncertainty__unit, domain=None, range=Optional[Union[str, UcumCode]])

slots.uncertainty__carried_to_participant_level = Slot(uri=EXPO.carried_to_participant_level, name="uncertainty__carried_to_participant_level", curie=EXPO.curie('carried_to_participant_level'),
                   model_uri=EXPO.uncertainty__carried_to_participant_level, domain=None, range=Optional[Union[bool, Bool]])

slots.linkage__spatial_linkage_unit = Slot(uri=EXPO.spatial_linkage_unit, name="linkage__spatial_linkage_unit", curie=EXPO.curie('spatial_linkage_unit'),
                   model_uri=EXPO.linkage__spatial_linkage_unit, domain=None, range=Union[str, "SpatialLinkageUnitEnum"])

slots.linkage__centroid_weighting = Slot(uri=EXPO.centroid_weighting, name="linkage__centroid_weighting", curie=EXPO.curie('centroid_weighting'),
                   model_uri=EXPO.linkage__centroid_weighting, domain=None, range=Optional[Union[str, "CentroidWeightingEnum"]])

slots.linkage__centroid_areal_unit = Slot(uri=EXPO.centroid_areal_unit, name="linkage__centroid_areal_unit", curie=EXPO.curie('centroid_areal_unit'),
                   model_uri=EXPO.linkage__centroid_areal_unit, domain=None, range=Optional[str])

slots.linkage__population_dataset = Slot(uri=EXPO.population_dataset, name="linkage__population_dataset", curie=EXPO.curie('population_dataset'),
                   model_uri=EXPO.linkage__population_dataset, domain=None, range=Optional[str])

slots.linkage__operation = Slot(uri=EXPO.operation, name="linkage__operation", curie=EXPO.curie('operation'),
                   model_uri=EXPO.linkage__operation, domain=None, range=Union[str, "LinkageOperationEnum"])

slots.linkage__buffer_radii_m = Slot(uri=EXPO.buffer_radii_m, name="linkage__buffer_radii_m", curie=EXPO.curie('buffer_radii_m'),
                   model_uri=EXPO.linkage__buffer_radii_m, domain=None, range=Optional[Union[float, list[float]]])

slots.linkage__network_mode = Slot(uri=EXPO.network_mode, name="linkage__network_mode", curie=EXPO.curie('network_mode'),
                   model_uri=EXPO.linkage__network_mode, domain=None, range=Optional[Union[str, "NetworkModeEnum"]])

slots.linkage__network_distance_m = Slot(uri=EXPO.network_distance_m, name="linkage__network_distance_m", curie=EXPO.curie('network_distance_m'),
                   model_uri=EXPO.linkage__network_distance_m, domain=None, range=Optional[float])

slots.linkage__network_time_min = Slot(uri=EXPO.network_time_min, name="linkage__network_time_min", curie=EXPO.curie('network_time_min'),
                   model_uri=EXPO.linkage__network_time_min, domain=None, range=Optional[float])

slots.linkage__intersection_min_overlap_pct = Slot(uri=EXPO.intersection_min_overlap_pct, name="linkage__intersection_min_overlap_pct", curie=EXPO.curie('intersection_min_overlap_pct'),
                   model_uri=EXPO.linkage__intersection_min_overlap_pct, domain=None, range=Optional[float])

slots.linkage__kernel_bandwidth_m = Slot(uri=EXPO.kernel_bandwidth_m, name="linkage__kernel_bandwidth_m", curie=EXPO.curie('kernel_bandwidth_m'),
                   model_uri=EXPO.linkage__kernel_bandwidth_m, domain=None, range=Optional[float])

slots.linkage__kernel_grid_resolution_m = Slot(uri=EXPO.kernel_grid_resolution_m, name="linkage__kernel_grid_resolution_m", curie=EXPO.curie('kernel_grid_resolution_m'),
                   model_uri=EXPO.linkage__kernel_grid_resolution_m, domain=None, range=Optional[float])

slots.linkage__geocoding_precision = Slot(uri=EXPO.geocoding_precision, name="linkage__geocoding_precision", curie=EXPO.curie('geocoding_precision'),
                   model_uri=EXPO.linkage__geocoding_precision, domain=None, range=Optional[Union[str, "GeocodingPrecisionEnum"]])

slots.linkage__geocoding_mixed_breakdown = Slot(uri=EXPO.geocoding_mixed_breakdown, name="linkage__geocoding_mixed_breakdown", curie=EXPO.curie('geocoding_mixed_breakdown'),
                   model_uri=EXPO.linkage__geocoding_mixed_breakdown, domain=None, range=Optional[str])

slots.linkage__geocoder = Slot(uri=EXPO.geocoder, name="linkage__geocoder", curie=EXPO.curie('geocoder'),
                   model_uri=EXPO.linkage__geocoder, domain=None, range=Optional[str])

slots.linkage__aggregation = Slot(uri=EXPO.aggregation, name="linkage__aggregation", curie=EXPO.curie('aggregation'),
                   model_uri=EXPO.linkage__aggregation, domain=None, range=Union[str, "AggregationEnum"])

slots.linkage__aggregation_n = Slot(uri=EXPO.aggregation_n, name="linkage__aggregation_n", curie=EXPO.curie('aggregation_n'),
                   model_uri=EXPO.linkage__aggregation_n, domain=None, range=Optional[int])

slots.linkage__participant_coverage_pct = Slot(uri=EXPO.participant_coverage_pct, name="linkage__participant_coverage_pct", curie=EXPO.curie('participant_coverage_pct'),
                   model_uri=EXPO.linkage__participant_coverage_pct, domain=None, range=Optional[float])

slots.linkage__coverage_unit = Slot(uri=EXPO.coverage_unit, name="linkage__coverage_unit", curie=EXPO.curie('coverage_unit'),
                   model_uri=EXPO.linkage__coverage_unit, domain=None, range=Optional[Union[str, "CoverageUnitEnum"]])

slots.linkage__study_area_coverage_pct = Slot(uri=EXPO.study_area_coverage_pct, name="linkage__study_area_coverage_pct", curie=EXPO.curie('study_area_coverage_pct'),
                   model_uri=EXPO.linkage__study_area_coverage_pct, domain=None, range=Optional[float])

slots.linkage__exposure_window = Slot(uri=EXPO.exposure_window, name="linkage__exposure_window", curie=EXPO.curie('exposure_window'),
                   model_uri=EXPO.linkage__exposure_window, domain=None, range=Optional[Union[str, "ExposureWindowEnum"]])

slots.linkage__exposure_window_years = Slot(uri=EXPO.exposure_window_years, name="linkage__exposure_window_years", curie=EXPO.curie('exposure_window_years'),
                   model_uri=EXPO.linkage__exposure_window_years, domain=None, range=Optional[int])

slots.linkage__exposure_window_detail = Slot(uri=EXPO.exposure_window_detail, name="linkage__exposure_window_detail", curie=EXPO.curie('exposure_window_detail'),
                   model_uri=EXPO.linkage__exposure_window_detail, domain=None, range=Optional[str])

slots.linkage__residential_history = Slot(uri=EXPO.residential_history, name="linkage__residential_history", curie=EXPO.curie('residential_history'),
                   model_uri=EXPO.linkage__residential_history, domain=None, range=Optional[Union[str, "ResidentialHistoryEnum"]])

slots.linkage__residential_history_detail = Slot(uri=EXPO.residential_history_detail, name="linkage__residential_history_detail", curie=EXPO.curie('residential_history_detail'),
                   model_uri=EXPO.linkage__residential_history_detail, domain=None, range=Optional[str])

slots.linkage__linkage_date = Slot(uri=EXPO.linkage_date, name="linkage__linkage_date", curie=EXPO.curie('linkage_date'),
                   model_uri=EXPO.linkage__linkage_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.linkage__relinkages = Slot(uri=EXPO.relinkages, name="linkage__relinkages", curie=EXPO.curie('relinkages'),
                   model_uri=EXPO.linkage__relinkages, domain=None, range=Optional[Union[Union[dict, Relinkage], list[Union[dict, Relinkage]]]])

slots.relinkage__date = Slot(uri=EXPO.date, name="relinkage__date", curie=EXPO.curie('date'),
                   model_uri=EXPO.relinkage__date, domain=None, range=Union[str, XSDDate])

slots.relinkage__reason = Slot(uri=EXPO.reason, name="relinkage__reason", curie=EXPO.curie('reason'),
                   model_uri=EXPO.relinkage__reason, domain=None, range=str)

slots.person__name = Slot(uri=EXPO.name, name="person__name", curie=EXPO.curie('name'),
                   model_uri=EXPO.person__name, domain=None, range=Optional[str])

slots.person__email = Slot(uri=EXPO.email, name="person__email", curie=EXPO.curie('email'),
                   model_uri=EXPO.person__email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$'))

slots.person__orcid = Slot(uri=EXPO.orcid, name="person__orcid", curie=EXPO.curie('orcid'),
                   model_uri=EXPO.person__orcid, domain=None, range=Optional[Union[str, CURIE]])

slots.person__role = Slot(uri=EXPO.role, name="person__role", curie=EXPO.curie('role'),
                   model_uri=EXPO.person__role, domain=None, range=Optional[str])


# Summary: "_Semantic Web for the Working Ontologist_"

## Chapter 1 - "What Is the Sematic Web"

Idea/vision: A "Web of Data" in the same form as the **Web of Links** (www) which we already know as linked webpages.
* Move from a web that presents its content to human being to an exchange of data between machines
* Instead of having one web page point to another, have one data item point to another via URIs
* Use a (new) data model to represent data in the Semantic Web, _Resourse Description Framework_ (RDF)
* Keep the ideology of the web we know with the AAA Slogan "**A**nyone can say **A**nything about **A**ny topic"
* For almost any topic you can find websites which wildely disagree with one another, this can be due to different reasons:
  * They may fundamentally disagree on some topic
  * Someone might want to intentionally deceive
  * Someone might simply be mistaken
  * Some information may be out of date
* The goal of the Semantic Web is not the get everyone to agree, but rather tries to cope in a world full of contradicting infomation and achieve some form of interoperability whithin it
* As a first requirement for making a statement about something on the web is to have a global way of identifying the thing we are talking about (here via gloabl URIs) _as for expample my idea of "Apple" is the company but your first thought is the fruit_
* The Semantic web opareates under a **Open World Assumption**, mean that there could always be new information introduced which would change the previously drawn conclusions, contrary to the now often used Closed World Assumption of common data bases
* Data in the Semantic Web is called **Linked Data**, as it can use the web addressing and linking capabilities to link data pieces between datasets across the web
 
## Chapter 2 - "Semantic Modeling"

How do we manage the tangled web of information that is the Semantic Web? Via **Modeling**
### Modeling for Human Communication
* Models can assist us in multiple ways: 
  * Models help people communicate
  * Models explain and can make predictions
  * Models mediate among multiple viewpoints
* Models for human communication:
  * Can make use of human interpretation to use a widely different form of language or just imagery 
  * However the same interpretation can also lead to (un-)intentional abuse e.g. in legislation
  * A collaborative style of document modeling is via _tags_, however the interpreation and usage of the same tags varies from person to person and the "bigger" a tag gets the more loosely related things will show up under the tags muddeling the modeling process
* Such models are _informal_ as the interpretation is up to human processing 
* To further clarify such models more layers have to be added which leads to heavily layered models such as again legislation
* Human communication is:
  * fundamental for the Semantic Web as it allows people to contribute to the growing body of knowledge and draw from it
  * not enough, as the data needs to be organized in a model in such a way that it can be useful to a wide range of consumers
### Explanation and Prediction
* Explanation makes resuse of a model easier and relates a conclusion to more basic principles
* Such principles are called _Formalisms_
  * Can be used for predictions
  * Allow evaluations to be independent of the consumer e.g. basic math as formalism (once you agreed to the conventions of it)
### Mediating Variability
* _Object-Oriented Programming_ (OOP) relies on the notion of a hierarchy of classes and subclasses for organizing
* Higher classes represent commonality among a large variety of entities and lower-classes represent commonality among a smaller, specific set of things
* The Sematic Web uses this idea of classes but allows different sources to say different things about them e.g. Information about Planets from astrological and astronomical sources
* This leads to models in the Semantic Web to be described in layers and thus merge models
### Expressivity in Modeling
* The same thing can be described in different _levels of expressivity_ e.g. modeling water molecules
* More expressive models are not inherently superior to models with less expressivity
* The Semantic Web uses differently expressive modeling languages which are all compatible with one another: (from least to most expressive)
  * **RDF** _Resource Description Framework_
  * **SHACL** _Shapes Constraint Language_
  * **RDFS** _RDF Schema Language_
  * **RDFS-Plus**
  * **OWL** _Web Ontology Language_
* All of these languages are supported by the _World Wide Web Constortium_ (W3C)

As different people will provide their own opinions on any topic, the Web will simultaneously contain organized and unorganized knowledge about the very same topic

## Chapter 3 - "RDF - The Basis of the Semantic Web"

### Distributing Data Across the Web
* Data is typically represented in tabular form
* However this form is not always ideal for either consumption or for merging different datasets
* The core idea is:
  * that regardless of where the data is stored that it can be accessed
  * any server needs to able to specify any property of an entitiy
* For this the Semantic Web is in need of global reference for column headings and rows (for data in tabular form)
* The RDF approach takes this a step further and stores the information in each cell of a table as a **triple**
* Each **triple** consists of: 
  * a _subject_ which is the identifier for the row
  * a _predicate_ (or _property_) which forms a statement about the relation of the subject
  * an _object_ which is the value of the cell
* A tiple can refer to the same entities with different statements, and thus form a directed graph 
* With this it is possible to merge infomation from multiple sources (but only when it is known which nodes in each of the source graphs match)
### Namespaces, URIs, and Identity
_URIs_ as a solution to know when a node in one graph is the smae node as in another graph 
* A URI provides a global identification for a resource that is common across the Web
* This global naming leads to a network effect (seen in the WWW)
* Any two Web applications in the world can refer to the same thing by referencing the same URI
* A node from one graph is merged with a node from another graph exactly if they have the same URI
* _IRI_ (Internationalized Resource Identifiers) are more generalized URI which can include characters from any language that has a standard web encoding 
* _CURIES_ (Compact URI) are a schematic representation of URIs in print and are accompanied by a declaration of the namespace correspondence
* CURIES allow a reader to more easily follow along a graph of information
* Examples of schemas for CURIES are _rdf, rdfs, skos, owl_
### Identifiers in the RDF Namespace
* _rdf:type_ is an example of a CURIE in _rdf_ which signifies a property that provides an elementary typing system in RDF
* To further enhance readability _Turtle_ syntax allows _rdf:type_ to be written as _a_ in RDF
### Higher Order Relationships
* In general it is often desired to make a statement about another statement e.g. Shakespeare wrote Hamlet in 1604
* This process is called _reification_ and can be achieved by using and merging triples!
* To express information about a statement e.g. Wikipedia says Shakespeare wrote Hamlet we use _explicit reification_ which in RDF standard is supported by _rdf:subject, rdf:predicate_ and _rdf:object_
### Naming RDF Graphs
* In a formal way, a graph is a set of triples, they might be highly connected or not at all
* A _named graph_ is a signled out set of triples (_graph_) which is given a name
* There are basic use cases for _named graphs_:
  * _One file, one graph_: If you want to keep data from different sources separate and thus put all the data from one source into single named graph
  * _Reification_: If you want to make statements about statements (as seen before) or even make a statement into a graph and then do statements about that graph
  * _Context_: If you would like to consider them in context e.g. an external link to an infomation source as imdb for movies
* Named graphs simply allow us to manage sets of these links and to name them as well
* Sometimes named graphs are referred to as _quads_ instead of triples
### Alternatives for Serialization
* **N-Triples**
  * Correspont most directly to the raw RDF triples
  * An ntriple file has the whole tirple on a single line
  * They are easy to ride from a file (parse) and to write into a file fro importing and exporting
* **Turtle/N3**
  * Is a more compact serialization of RDF _Turtle_ which is intself a subset of a syntax called _N3_
  * Turtle begins with a preamble in which bindings between the (local) CURIEs and the (global) URIs are definded.
  * Turtle also provides for a compact representation of data as it can use ";" to indicate that another triple with the same subject follows, or uses a "," to seperate objects
  * **RDF/XML** and **JSON-LD** are two more ways to serialize triples in their given environment
 ### Blank Nodes
 * Are used to represent a resource that has no identity on the web
 * _Blank nodes_ represent in logical terms the statement: "there exists"
 Additionally RDF provides a facility for ordering elements in a list format via Turtle, _N-Quads_ provides serializations for triples for use with named graphes and _TriG_ is a Turtle extension which lets us express several graphs in a single file
 
 ## Chapter 4 - "Semantic Web Application Architecture"
 ### RDF Parser/Serializer
 * A RDF parser takes files such as .csv as input and converts it into an internal representation of the triples that are expressed in that file e.g. Cube Creator is a RDF parser
 * Generally it is not given that reading in and exporting a RDF file again will result in the exported file to be identical to the input file
 * RDF parsers map the meta data to the values of the input file
 * _R2RML_ (Relational To RDF Markup Language) and _Direct Mapping_ are ways of mapping meta data from relational databases. Their job is to provide enough information about the mapping of a table to RDF that we do not have to second guess any of those things
 * Another rich data source comes from HTML pages.
 * A key capability provided by the ability to embed data in web pages is called _rich snippets_ which refers to the inclusion of structured data in the display of a search result
 * Ways of embedding RDF data into an HTML web page include _Microdata, RDFa and JSON-LD_ 
### RDF Store
* Typically a RDF store is accompanied by aa parser and a serializer to populate the store and publish information from the store
* includes as a fundamental capability the ability to merge two datasets together
* Any resources with the same URI are considered to be equivalent in the merged dataset
* The query language for RDF is _SPARQL_
* _SPARQL endpoints_ provide access to large amounts of structured RDF data in the RDF stores (globally)
* RDF query languages look more like statements in predicate calculus
* _SPARQL_ has little need for a subquery construct as in many cases the same effect can be achieved with just a single query
### Application Code
* RDF capabilities are provided as Application Programming Interface (API) bindings for that language
* Typical RDF applications include: _calendar integration, map integration, annotation, content management_
* Data can remain in the RDF store itself thus being private where as other data can be used by applications e.g. train timetables
* In this sense information on a single RDF-backed web page typically comes from multiple sources
A semantic model acts as sort of glue between disparate, federated data sources so we can describe how they fit together
## Chapter 5 - "Linked Data"
### Weaving a Web of Data
* A web of data consists of data from around the world taht is linked together so it can be browsed, crawled, integrated etc. with the core idea behind being _linked data_
* Web of data uses RDF to write data descriptions that include links to other data descriptions
* Three rules for data publications for weaving a web of data:
  * HTTP URIs to name everything: they provide a default mechanism to obtain descriptions
  * When accessing an HTTP URI the server must provide descriptive informaion about the resource identified by that URI using the Web standard languages
  * For provided descriptive data the server must include links to HTTP URIs of other things so that Web clients can find more things by looking up these new HTTP URIs recursively
 * URIs allow us to make vocabulary and resource identification unambiguous by providing a global identification mechanismfor the terms and subejcts of our descriptions
 * URIs also have a _dereferencing_ mechanism which uses the URI to find a location on the Web from which furhter information can be loaded
 * By using URIs we provide junction points that allow us to merge the datasets regardless of their provenance
 * When using URIs we need to be precise our description, the best practice is to use different URIs to identify different resources e.g. talking about the size of a cat or the size of the picture of the cat you are referencing to
 * _Dereferencing_ of HTTP URIs is a cornerstone of the hypertext Web
 *  URIs are standardize in _Request for Comments_ RFCs a particulatr format which is key for minting URIs
 *  HTTP URIs allow us to use the full infrastructure of the hyptertext Web, namely:
   * The _Domain Name Service_ DNS
   * _Content Negotiation_, which allows a Web server to serve different content for the same HTTP URI to different clients
   * _HTTP Redirection_ which allows a server to redirect a reference to another adress
 * The _host_ part of an HTTP URI is managed by the DNS so a _domain name_ e.g. [wikipedia.org](http://wikipedia.org), has to be registered
 * A broken link can mean loss of access to an entire dataset!
 * The Cool URI proposal on making URIs stable:
   * Design URIs with reference to as few implementation details as possible e.g. avoid language-dependent extensions such as .PHP or specific server names, software, portnumbers etc.
   * Web servers are able to negotiate content based on information from Web clients
   * Avoid adding version information from stable URIs
   * Often the original data source already has some kind of identifier e.g. primary key, account numbers, use these to ensure the URI corresponds to the right data elements
 ### HTTP and the Architecture of the Web
 * The use of domain names provides stable URIs, allowing a data provider to change a server's adresses without changing the URIs of the data that is hosted there
 * Using the HTTP protocol, a Web client can negotiate the content of a response to an HTTP URI lookup, which is _content negotitation_ or _conneg_ which is the mechanism
 * HTTP content negotiation can be used by linked data applications to negotiate the RDF syntax they prefer e.g. XML, Turtle, JSON-LD, etc. or alternate representations for their interfaces
 * _HTTP redirection_ allows us to avoid broken links
 * 303 response to an HTTP URI means that the service that the DNS referred the URI to is unable to provide a representation of the target source but it can refer the requester to another resource instead
 ### Hash or Slash
 * There are two choices for the ending parts of a URI which impact performance in dereferencing it:
   * _Hash URIs_
   * _Slash URIs_
 * _Hash URIs_ contain the hash character "#" which is the technical mark of a fragment identifier inside the URI
 * Traditionally the "#" is used to denote a fragment of a web page e.g. a specific part of a web page which the URI would scroll down to
 * Using framgents has two advangtages:
   * It differentiates between the name of the descriptions and the names of the resources described without performing redirection
   * It allows grouping of several descriptions in a single resource that can be cached by a client to avoid several calls to discover different linked resources
 * However this means that accessing the address one cannot obtain the description of just a single resource
 * _Slash URIs_ use the "/" to generate identifiers, also called "303 URIs"
 * They use the "/" to redirect accesses to the HTTP URI of a thing to some URL where to find a description of that thing
 * This works in a four step process:
   * Client attempts to connect to the HTTP Slash URI
   * Server responds with "303 See Other" and provides the URL to get a description
   * Client performs a second HTTP GET to the URL
   * Server then provides the requested description "200 OK"
 * Slash URI allow us to be much more modular but doubles the amount of calls needed compared to hash URIs
 * Thus _hash URI_ are typically used for smaller data sets where grouping makes sense such as vocabularies, ontologies or schemas
 * The two options can also be mixed by adding the "#" to an existing slash URI
 ### Further Notes
 * External links can be established in different ways:
   * A new dataset can create its own URIs for common entries. Often not created to be part of the Web of data. However linkage can be established later on by identifiying the fact that some URI in the new datasets acutally refers to an entity that already has a URI in another dataset
   * Make the effort to reuse URIs that already have been established by existing datasets. Altough time consuming it brings pay off in the long run. Another option is to link the dataset to a schema, like RDFS, RDFS-Plus, SKOS or OWL. These define metadata entities like _classes_ and _properties_ that can be used to aglin data
   * Often a standard is already available for some entities but has not been published as linked data e.g. ISO publishing short codes for countries
 ## Chapter 6 - "Querying the Semantig Web - SPARQL"
 ### Tell-and-Ask Systems
 * Tell-and-ask is a simple system where it gets told some facts and in return it can answer questions based on what it was told
 * Most tell-and-ask systems do not use natural language to get answers and the languages are usually very precise and technical
 * An example for a tell-and-ask system would be a classic adressbook or just in general spreadsheets
 * However spreadsheets sometimes do have difficulties representing data from multiple sources and rely on the person entering the data for naming the columns etc.
 * Avanced tell-and-ask systems are called relational databases
 * Relational databases do have the ability to answer questions about thing that come from multiple sources
 * This comes at the price of requiring a specialized language for querying the database (_query language_)
### RDF as a Tell-and-Ask System
* Unlike for rational databases, the cross-references are not visible to the end user in RDF systems, and there is no need to explicitly represent them in the query language
### SPARQL - Query Language for RDF
* The syntax of SPARQL looks a lot like Turtle
* Putting "?" before for example "movie" (?movie) will make into a question word and it acts as a "variable"
* For example ":director" refers to a resource with the ":" infront
* To be more precise properties like ":directedBy" should be used instead of ":director" for easier readability for the end user
* SPARQL provides a way of asking about the metadata of triples as well
* SPARQL is able to to do arithmetic and comparisons on all XML data types as well as XPATH standard like REGEX and Boolean functions for AND, OR and NOT
* SPARQL also provides a tool for creating triples or rather models via the command CONSTRUCT
* With SPARQL it is possible (and necessary) to transform hierachical data e.g. lineage trees
**This section contains a LOT of examples, it is recommended to look at them for a general understanding of SPARQL querying**
## Chapter 7 - "Extending RDF: RDFS and SHACL"
There are two basic ideas at play in these extensions:
* _Inference_: Drawing conclusions based on data we have already seen
* _Expectations_: Form some prediction about data we have not yet seen (_Shapes Constrain Language_ (SHACL))
### Inference in RDF with RDFS
* RDFS stands for RDF Schema _rdfs:_
* Used for example in context _rdfs:subClassOf_ in the RDFS language. This lets us make make inference e.g. "Tshirt" is a subclass of "Shirt" meaning that if we know an object to be a "Tshirt" we can infer that it is also of the class "Shirt"
* The strategy of basing the meaning of our terms on inferencing provides a robust solution to understanding the meaning of novel combinations of the terms
* RDFS can deal with the issue of _multiple inheritance_ (where a single subclass is of two distinct classes) by just applying the rule _subClassOf_ for each _class_
### Where are the Smarts?
* The power ofa query engine with inferencing capability is determined by the set of inferences that it supports (RDFS has a small set, OWL supports the larger set of OWL inferences)
* _Asserted triples_ are triples which are asserted in the original RDF store
  * The store was populated by merging triples from many sources and thus all the triples are asserted
* _Inferred triples_ are triples which are inferred by one of the inference rules that govern a particulare inference engine
  * It is possible to infer a triple which has been already asserted which then will consider the triple to have been asserted
* There is no lagical distinction betweeen asserted and inferred triples
* When merging the information from multiple sources the situation bcecomes subtle where each source itself is a system that includes an inference engine
### When Does Inferencing Happen?
* Simplest approach: Store all triples in a single store regardless whether they are asserted or inferred (_cached inferencing_ or _materialized inferencing_)
* In _just in time inferencing_ triples are actually never stored and inferencing is done in response to queries only
### Expectation in RDF
* In some situations in which we are not interpreting data, we instead are acting on some expectations about the data in the wild
* Expectation in the Semantic Web can take three broad forms:
  * _Data validation_: Data found in the wild purports to describe a particular thing
  * _Soliciting user input_: Request input from a user. Typically in form of a wizard
  * _Validating user input_: Even though we communicate our expectations to a user, they might not provide data in the form we expect
* The expectations for a data description is like a specification of the _shape_ that the data should take
* Expectation can also place constraints on values
* Each of the constraints can say something differnent about the property
* One possible validation is _SHACL validation_
* If we want to ensure interoperability between open and heterogenous systems, we need a way to specify our expectations about the data they will provide and consume
* SHACL provides the content for form to fill in in terms of field names, types, and allowable values that the forms should have e.g. HTML
* SHACL helps us to retain the value of the data wilderness while, to some extent, taming its wild nature
## Chapter 8 - "RDF Schema"
### Schema Languages and Their Functions
* For a given schema, it is possible to determine (often automatically) whether a particular document conforms to that schema
* The schema tells us something about the information that is expressed in the system
* The schema is information about the data
* XML Stylesheet Definition (XSD) defines Styles in an XML Language
* In case of RDF the schema language (RDFS), all schema information in RDFS is defined with RDF
* In RDFS, we express meaning through the mechanism of inference
### The RDF Schema Language
* Defining the "meaning" of a distinguished resource _rdfs:subPropertyOf_
* _rdfs:subPropertyOf_ has no direct analog in OOP where properties are not first-class entities (i.e. they cannot be related to one another, independent of the class in which they are defined)
* When we describe the usage of terms in our data, we would also like to represent how property is used relative to the defined classes
* _rdfs:domain_ and _rdfs:range_ are two stipulations expressed in RDFS
* The _domain_ of a function is the set of values for which it is defined, and the _range_ is the set of values it can take
* In RDFS, there is no way to assert that a particular individual is not a member of a particular class and there is no notion of an incorrect or inconsistent inference
* Whenever we specify the _rdfs:domain_ of a property to be some class, we can also infer that the property also has any superclass as _rdfs:domain_. Same for _rdfs:range_
* We can draw conclusions about the type of any element based simply on its use in a single tirple whenever we have domain or range information about the predicate
* In RDFS there is no notion of inheritance per se
* Anything we say about members of the parent class will necessarily hold for all instances of the subclass
* Seen from an OO point of view, this interaction seems like inheritance up the tree - in other words, just the opposite of what is normally expected of inheritence in OOP
### RDFS Modeling Combinations and Patterns
* RDFS can not infer **set intersections**, meaning it can only approximate it by supporting the inferencing in on direction (it can see that x is member of C and C is part of A and B it works however if but only from knowing membership in A and B we cannot infer membership in C p.228)
* **Set union** work similarly, we can only draw inference in one direction
* **Property union** _rdfs:subPropertyOf_ can be used to combine properties from different sources in a way that is analogous to the way in which _rdfs:subClassOf_ can be used to combine classes as a (pseudo-)union.
* **Property transfer**: When modeling the relationship between information that comes from multiple sources, a common requirement is to state that if two entities are related by some relationship in one source. 
* Property transfer can be used to link properties together you can link your own ":author" to the widely used "dc:creator" and state that they are the same (which then links the data)
### Challenges
* Domains and ranges are not used to validate information but instead are used to determin enew information based on old information
* They are best understood as tools for knowledge discorvery rather than knowledge description
### Modeling with Domains and Ranges
* If a thing is a member of two domains, inference will lead to the conclusion that each thing that is part of both domains will land in the intersection of the two classes specified in the domain statements
* The two properties can be merged by mapping both properties to a third, domain-neutral property which does not need any information at all
### Nonmodeling Properties in RDFS
* RDFS also provides a handful of properties that have no defined inference semantics e.g. _rdfs:label_ which describes the ways in which display agents interact with the model
* anther one is _rdfs:seeAlso_ which has no formal semantic
* _rdfs:isDefindedBy_
* _rdfs:comment_
## Chapter 9 - "RDFS-Plus"
* Is a variation of RDFS with an additional set of OWL constructs to further increase the inference capability of RDFS with less complexity than OWL as a whole
* Serves as pedagagical stepping stone between RDFS and OWL (so I think looking at the examples in the book will provide useful for grasping the concepts)
### Inverse
* _owl:inverseOf_: Is the inverse of a property which is another property that reverses its direction (is NOT equal to the _opposite_!)
* Works in a more mathematical way, as for example the inverse of _lit:wrote_ would be could be _lit:writtenBy_ (if definded so by the _lit:wrote owl:inverseOf lit:writtenBy_ property)
* An advantage to represent such relationships in RDFS-Plus is that all the relatiionships among these properties are represented in a single model, and can even be displayed visually
* _owl:inverseOf_ lets us for example define _superclasses_ if the superclass is defined as _rdfs:subClassOf owl:inverseOf rdfs:superClassOf_ 
* This differs from the previous triple in that the subject is a resource in the RDFS namespace. However this can be problematic as it is normally possible to dereference an HTTP URI to learn more about its resource and in this case since _rdfs:superClassOf_ is not definded by the W3C the attempt would fail 
* In other words "just because you are allowed to say something, doesn't mean that you should"
* _owl:SymmetricProperty_ defines that if a property e.g. _bio:married a owl:SymmetricProperty_ then _bio:married_ goes both ways A is married to B and thus it can be inferenced that B is married to A
* _owl:TrasitiveProperty_: defines that the property also applies to previous parts of the graph e.g. ancestors, which If A is ancestor of B and B ancestor of C that means A is also an ancestor of C
### Managing Networks of Dependencies
* I advise to look at the example with the cooking recipe for more understanding of a more complex model and how it manages dependencies between the steps of the cooking process
### Equivalence
* It is not necessarily the case that any two stakeholders will use the same URI to refer to the same entity
* Althought there are ways to stipulate that two URIs actually refer to the same entity, there are different ways in which two entities can be the same
* _owl:equivalentClass_ sets two calsses to equivalent
* It means that the two classes have the same members but not that other properties of the classes are shared
* _owl:equivalentProperty_ behaves in a similar way as the subClassOf "trick"
* These two provide intuitive ways of expressin relationships that were already expressible in RDFS (but with a bit more hoops to jump through)
* With _owl:sameAs_ it is possible to refer to _individuals_ and link datasets together e.g. Shakespeare from a literature database to the town register
### Merging Data from Different Databases
* It is not uncommon for differnt databases to overlap in inexact ways e.g. products of the same company but in different facilities might not be all complete or defined slightly different
* This can be solved by the _owl:sameAs_ statement, but as databases tend to change frequently, assinging the properties by hand seems very inefficient
### Computing Sameness: Functional Properties
* Functional properties borrow their name from mathematics and are ones that for which there can be just one value e.g. hasBirthplace
* We want to desribe something as being able to refer to only a single value
* _FunctionalProperty_ and _InverseFunctionalProperty_ use this idea to determine when two resources refer to the same individual (p.279)
* In most real cases _InverseFunctionalProperty_ will be used to define sameness and it refers to the inverse of the _FunctionalProperty_ e.g. if math:hasSquare is a funtional property then its inverse math:hasSquareRoot, is an inverse functional property
* Functional properties are fairly commonplace e.g. any identifying number (social securitynumber, driver's license number, etc.) is an inverse functional property
* The challenge is to find an inverse functional property that is present in both datasets that we can use to bridge between them
* **Functional only** - hasBirthdate is a functional property only. Someone has exaclty one birthdate but manny people can share the same birthday
* **Inverse functional only** - hasDiary is an inverse functional property only. A person may have many diaies, but it is the nature of a diary that it is not a collaborative effort; it is authored by one person only
* **Both functional and inverse functional** - taxID is both inverse functional and functional, since we want there to be exactly one taxId for each person and exactly one person per taxID
## Chapter 10 - "Using RDFS-Plus in the Wild"
* Applications include _Schema.org_, the US government effort called Data.gov and _FOAF_ "Friend of a Friend", a project dedicated to creating and using machine-readable hompages that describe people.
* In this chapter I will focus mainly on _Schema.org_ as it is used by Zazuko's Cube Creator tool in the backend for their URIs
### Schema.org
* It is a joint effort started by Google, Microsoft, Yahoo and Yandex to provide shared ontologies supporting the embedding of structured data in web pages  (for rich snippets and enhanced search engine optimization)
* However these applications cannot do their job without some sort of shared vocabulary for that data
* _Schema.org_ provides a central location for this shared vocabulary
* It provides a way of referencing to data on the web. By marking the data with _Schema.org_ it can be embedded into web pages by using any of the formats RDFa, Microdata or JSON-LD (Which the aim of OGD and in the end the Visualize tool is)
## Chapter 11 - " SKOS - Managing Vocabularies with RDFS-Plus"
### Simple Knowledge Organization System (SKOS)
* The key differentiator between SKOS and existing thesaurus standards is its basis in the Semantic web
* SKOS was designed from the start to allow modelers to create modular knowledge organizations that can be rused and referenced across the Web
* A design goal of SKOS was also that it is possible to map any thesaurus standards to SKOS in a fairly straightforward way
* In SKOS are _Concepts_: They are ways to describe published works and unlike classes in RDFS, concepts in SKOS have no formal correspondence in mathematics
* SKOS maintains internationalization in language as each concept has labels in multiple languages and none take precedence over any other (labels with i.e "en" or "de")
* SKOS defines three different kinds of labels: a _preffered label_, an _alternative label_ and a _hidden label_
* Each property has an _rdfs:label_ which provides a human-readable versionn of the name of each resource
* More than one value for _rdfs:label_ can be inferred, the challenge comes in how to display such a resource with multiple print names
### Semantic Relations in SKOS
* SKOS defines several "semantic relations", properties that relate concepts to one another, corresponding to familiar terms like _broader, narrower,_ and _related_ from thesauerus standards
* _skos:related_ : corresponds to familiar thesaurus relations
* _skos:narrower_ and _skos:broader_ are subproperties of transitive properties (_skos:broaderTransitive, skos:narrowerTransitive_). However _skos:related_ is not but is an _owl:SymmetricProperty_
* _skos:narrower_ is the inverse of _skos:broader_
* SKOS does not represent transitive nature of subClassOf directly, but instead uses a more sophisticated model, in which the user of the model can decide if they want to use a transitive notion of broader or narrower, or not
* The relationship is expressed informally in SKOS as it (sometimes) needs interpretation to the meaning of the annotation (e.g. which term is the broader of the two in the triple)
* If there were an inference-based defnition of the semantics of broader or narrower in SKOS then the intended direction of the statements would be explicit, however it is not
* One of the main advantages of SKOSis that it allows vocabularies to be linked
* In a world of computer networks, it is now common for vocabularies to interact and since SKOS is represented in RDF, every term has a URI which can be referenced on the Web
* _skos:exactMatch_ does not have any inference-based semantics, but it does have a conventional meaning that the two terms can be used interchangably across a wide range of information retrieval applications
### Concept Schemes
* A _concept scheme_ is a largerly informal collection of concepts, corresponding roughly to a particular thesaurus or konwledge organization system
* There are no conditions that membership in a concept scheme be related in any way to the semantic relations (_broader, narrower, or related_
* A concept can be in one concept scheme while its broader and narrower concepts are in another
* Concepts are related to a concept scheme by the properties _skos:inScheme, skos:hasTopConcept_ and _skos:topConceptOf_
* In this way a concept scheme can also have one or more distinguished concepts called _Top Concepts_
* The relationship between top concepts and other members of a concept is described with two tiples (p.330) and the top concept of a scheme must also be in that schmee, and the properties topConceptOf and hasTopConcept are inverses
* The property _exactMatch_ makes much less commitment to interchangeability of concepts, indicating only that one concept acts like the other in information retrieval settings
### SKOS Integrity
* There are a number of integrity conditions that can be applied to any SKOS model to verify that it conforms to the standard
* Many of the constraints can be (and are) expressed in RDFS
* Meaning that if a concept C is _inScheme_ S, then S in turn must be a member of _skos:ConceptScheme_
### SKOS in Action
* Utilization of SKOS standard has grown dramatically since the W3C made it a recommendation
* Before SKOS there was no standard way to represent a vocabulary in digital form
* A number of factors have driven its popularity:
  * Its **Simplicity**: Just about any other vocabulary system can be translated to SKOS without a lot of effort
  * The **Ease of Transformation** from other systems into SKOS. For the most part, if it is possible to query an existing vocabulary for _broader, narrower_, and _related_ terms, then the vocabulary can be converted directly into SKOS
  * Translation of a vocabulary into SKOS involves sleection a **Globally Unique Identifier** for each concept. This provides a great advantage when relating vocabularies to one another
* The translation of terms into URIs makes it possible to relate things with a single triple
## Chapter 12 - "Basic OWL"
### Restrictions

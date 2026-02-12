Here’s a polished and corrected version of your document. I focused on improving clarity, grammar, and flow while keeping your technical accuracy intact. I also standardized formatting and fixed minor inconsistencies:

---

# Shape Trees

Shape Trees are based on data shapes found in SolidOS GitHub repositories.

They provide intuitive **data boundaries** that enable human-to-machine interoperability.

> Shape Trees combine RDF vocabularies, shapes, and resources into “things” that serve as detailed blueprints for machine-to-machine interoperability. At the same time, they allow us to model concepts that people can easily understand, such as a chat room, a calendar of appointments, or an event stream from a medical device. Using Shape Trees, we can define data boundaries that both machines can interact with reliably and humans can comprehend.

---

## Key Ideas

A **boundary** defines a unit of data. Think of it as a container for a set of logically related information.

**Examples:** A photo album, a medical record, a calendar, or a chat room.

Everything inside this boundary is logically connected.

### Intuitive for Humans

Data should be grouped in a way that matches how people naturally think about it.

**Example:** A user can share “my photo album” instead of manually selecting dozens of individual images.

### Machine-Readable for Interoperability

Applications require a precise definition of what a boundary contains.

Shape Trees specify the resources and relationships inside a boundary, enabling apps to read, write, and validate data consistently.

### Secure Collaboration

Boundaries simplify permissions. You can share the entire boundary (e.g., an album) rather than micromanaging individual files.

This approach reduces accidental over-sharing and preserves the integrity of data relationships.

---

## Shape Trees = Schema + Grouping

Shape Trees combine **RDF vocabularies** (data definitions) and **shapes** (validation rules) with a hierarchical organization of resources.

### Dual Purpose

* **Machine-readable:** Apps can reliably manipulate and interoperate over the data.
* **Human-readable:** People interact with recognizable “things” like albums, calendars, or events instead of abstract RDF triples or file hierarchies.

---

## How to Create a Shape Tree

### 1. Define the “Thing”

A Shape Tree represents a logical unit of data - a concept that people understand.

**Examples:**

* **Meeting** → A calendar event with participants, time, location, agenda
* **PersonalProfile** → A person’s basic information: name, email, bio, profile picture

### 2. Identify Resources / Sub-resources

List all resources and sub-resources that make up the thing. These form the nodes in the tree.

**Example: Meeting**

* Meeting (root node)

  * Title
  * StartTime
  * EndTime
  * Location
  * Participants (list of people)
  * Agenda (optional document)

**Example: PersonalProfile**

* PersonalProfile (root node)

  * Name
  * Email
  * Photo
  * Bio
  * SocialLinks (optional list)

### 3. Choose a Vocabulary

Use standard RDF vocabularies whenever possible to ensure machines understand semantics.

* **FOAF (Friend of a Friend)** → foaf:Person, foaf:name, foaf:mbox
* **Schema.org** → schema:Event, schema:location, schema:attendee
* **VCARD** → vcard:hasEmail, vcard:hasPhoto

### 4. Define Shape Constraints

Use **SHACL** or **ShEx** to define rules for what is allowed in the tree.

---

## Reference Source Files

### Profile

* [editProfile.view.ts](https://github.com/SolidOS/profile-pane/blob/022cb2458371efdee74d781d7203703d4f524ac1/src/editProfilePane/editProfile.view.ts#L47)
* [Ontology folder](https://github.com/SolidOS/profile-pane/tree/main/src/ontology)
* [profileForm.ttl](https://github.com/SolidOS/profile-pane/blob/main/src/ontology/profileForm.ttl)
* [socialMedia.ttl](https://github.com/SolidOS/profile-pane/blob/main/src/ontology/socialMedia.ttl)

### Preference

* [basicPreferences.ts](https://github.com/SolidOS/solid-panes/blob/540133ac84232b8d7e6da494691a3fec11707d7c/src/dashboard/basicPreferences.ts#L60)

### Schedule

* [schedulePane.js](https://github.com/SolidOS/solid-panes/blob/540133ac84232b8d7e6da494691a3fec11707d7c/src/schedule/schedulePane.js#L569)
* [formsForSchedule.ttl](https://github.com/SolidOS/solid-panes/blob/main/src/schedule/formsForSchedule.ttl)

### Forms

* [pane.js](https://github.com/SolidOS/solid-panes/blob/540133ac84232b8d7e6da494691a3fec11707d7c/src/form/pane.js#L125)

### Contacts

* [individual.js](https://github.com/SolidOS/contacts-pane/blob/cf49efe007b6b7b0f13b0be8fca897cc35fcc628/src/individual.js#L77)
* [Ontology folder](https://github.com/SolidOS/contacts-pane/tree/main/src/ontology)
* [forms.ttl](https://github.com/SolidOS/contacts-pane/blob/main/src/ontology/forms.ttl)
* [organizationForm.ttl](https://github.com/SolidOS/contacts-pane/blob/main/src/ontology/organizationForm.ttl)
* [vcard.ttl](https://github.com/SolidOS/contacts-pane/blob/main/src/ontology/vcard.ttl)

### Issue Tracker

* [Ontology folder](https://github.com/SolidOS/issue-pane/tree/9c24db98fb810ad2139244f8f1552fc0f704c1ac/src/ontology)
* [trackerSettingsForm.ttl](https://github.com/SolidOS/issue-pane/blob/9c24db98fb810ad2139244f8f1552fc0f704c1ac/src/ontology/trackerSettingsForm.ttl)
* [ui.ttl](https://github.com/SolidOS/issue-pane/blob/9c24db98fb810ad2139244f8f1552fc0f704c1ac/src/ontology/ui.ttl)
* [wf.ttl](https://github.com/SolidOS/issue-pane/blob/9c24db98fb810ad2139244f8f1552fc0f704c1ac/src/ontology/wf.ttl)

### Meeting

* [meetingDetailsForm.ttl](https://github.com/SolidOS/meeting-pane/blob/main/src/meetingDetailsForm.ttl)

### Chat

* [Shapes folder](https://github.com/SolidOS/chat-pane/tree/main/shapes)
* [chat-shapes.shex](https://github.com/SolidOS/chat-pane/blob/main/shapes/chat-shapes.shex)
* [chat-shapes.ttl](https://github.com/SolidOS/chat-pane/blob/main/shapes/chat-shapes.ttl)
* [chatPreferencesForm.ttl](https://github.com/SolidOS/chat-pane/blob/main/shapes/chatPreferencesForm.ttl)


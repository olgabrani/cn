# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class MdlAssign(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    alwaysshowdescription = models.IntegerField()
    nosubmissions = models.IntegerField()
    submissiondrafts = models.IntegerField()
    sendnotifications = models.IntegerField()
    sendlatenotifications = models.IntegerField()
    duedate = models.BigIntegerField()
    allowsubmissionsfromdate = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requiresubmissionstatement = models.IntegerField()
    completionsubmit = models.IntegerField()
    cutoffdate = models.BigIntegerField()
    teamsubmission = models.IntegerField()
    requireallteammemberssubmit = models.IntegerField()
    teamsubmissiongroupingid = models.BigIntegerField()
    blindmarking = models.IntegerField()
    revealidentities = models.IntegerField()
    attemptreopenmethod = models.CharField(max_length=10)
    maxattempts = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assign'

class MdlAssignGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    grader = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    attemptnumber = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assign_grades'

class MdlAssignPluginConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    plugin = models.CharField(max_length=28)
    subtype = models.CharField(max_length=28)
    name = models.CharField(max_length=28)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_assign_plugin_config'

class MdlAssignSubmission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    status = models.CharField(max_length=10, blank=True)
    groupid = models.BigIntegerField()
    attemptnumber = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assign_submission'

class MdlAssignUserFlags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    assignment = models.BigIntegerField()
    locked = models.BigIntegerField()
    mailed = models.IntegerField()
    extensionduedate = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assign_user_flags'

class MdlAssignUserMapping(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assign_user_mapping'

class MdlAssignfeedbackComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    commenttext = models.TextField(blank=True)
    commentformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_comments'

class MdlAssignfeedbackFile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    numfiles = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignfeedback_file'

class MdlAssignment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    assignmenttype = models.CharField(max_length=50)
    resubmit = models.IntegerField()
    preventlate = models.IntegerField()
    emailteachers = models.IntegerField()
    var1 = models.BigIntegerField(blank=True, null=True)
    var2 = models.BigIntegerField(blank=True, null=True)
    var3 = models.BigIntegerField(blank=True, null=True)
    var4 = models.BigIntegerField(blank=True, null=True)
    var5 = models.BigIntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField()
    timedue = models.BigIntegerField()
    timeavailable = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignment'

class MdlAssignmentSubmissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    numfiles = models.BigIntegerField()
    data1 = models.TextField(blank=True)
    data2 = models.TextField(blank=True)
    grade = models.BigIntegerField()
    submissioncomment = models.TextField()
    format = models.IntegerField()
    teacher = models.BigIntegerField()
    timemarked = models.BigIntegerField()
    mailed = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignment_submissions'

class MdlAssignsubmissionFile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    numfiles = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignsubmission_file'

class MdlAssignsubmissionOnlinetext(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    onlinetext = models.TextField(blank=True)
    onlineformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_assignsubmission_onlinetext'

class MdlBackupControllers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backupid = models.CharField(unique=True, max_length=32)
    operation = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    itemid = models.BigIntegerField()
    format = models.CharField(max_length=20)
    interactive = models.IntegerField()
    purpose = models.IntegerField()
    userid = models.BigIntegerField()
    status = models.IntegerField()
    execution = models.IntegerField()
    executiontime = models.BigIntegerField()
    checksum = models.CharField(max_length=32)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    controller = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_backup_controllers'

class MdlBackupCourses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField(unique=True)
    laststarttime = models.BigIntegerField()
    lastendtime = models.BigIntegerField()
    laststatus = models.CharField(max_length=1)
    nextstarttime = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_backup_courses'

class MdlBackupFilesTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backupid = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    filearea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    info = models.TextField(blank=True)
    newcontextid = models.BigIntegerField(blank=True, null=True)
    newitemid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_backup_files_template'

class MdlBackupIdsTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backupid = models.CharField(max_length=32)
    itemname = models.CharField(max_length=160)
    itemid = models.BigIntegerField()
    newitemid = models.BigIntegerField()
    parentitemid = models.BigIntegerField(blank=True, null=True)
    info = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_backup_ids_template'

class MdlBackupLogs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backupid = models.CharField(max_length=32)
    loglevel = models.IntegerField()
    message = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_backup_logs'

class MdlBadge(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    issuername = models.CharField(max_length=255)
    issuerurl = models.CharField(max_length=255)
    issuercontact = models.CharField(max_length=255, blank=True)
    expiredate = models.BigIntegerField(blank=True, null=True)
    expireperiod = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    message = models.TextField()
    messagesubject = models.TextField()
    attachment = models.IntegerField()
    notification = models.IntegerField()
    status = models.IntegerField()
    nextcron = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_badge'

class MdlBadgeBackpack(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    email = models.CharField(max_length=100)
    backpackurl = models.CharField(max_length=255)
    backpackuid = models.BigIntegerField()
    autosync = models.IntegerField()
    password = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_badge_backpack'

class MdlBadgeCriteria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    badgeid = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria'

class MdlBadgeCriteriaMet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    issuedid = models.BigIntegerField(blank=True, null=True)
    critid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datemet = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria_met'

class MdlBadgeCriteriaParam(models.Model):
    id = models.BigIntegerField(primary_key=True)
    critid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_badge_criteria_param'

class MdlBadgeExternal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    backpackid = models.BigIntegerField()
    collectionid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_badge_external'

class MdlBadgeIssued(models.Model):
    id = models.BigIntegerField(primary_key=True)
    badgeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    uniquehash = models.TextField()
    dateissued = models.BigIntegerField()
    dateexpire = models.BigIntegerField(blank=True, null=True)
    visible = models.IntegerField()
    issuernotified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_badge_issued'

class MdlBadgeManualAward(models.Model):
    id = models.BigIntegerField(primary_key=True)
    badgeid = models.BigIntegerField()
    recipientid = models.BigIntegerField()
    issuerid = models.BigIntegerField()
    issuerrole = models.BigIntegerField()
    datemet = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_badge_manual_award'

class MdlBlock(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40)
    version = models.BigIntegerField()
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    visible = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_block'

class MdlBlockCommunity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    coursename = models.CharField(max_length=255)
    coursedescription = models.TextField(blank=True)
    courseurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_block_community'

class MdlBlockInstances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockname = models.CharField(max_length=40)
    parentcontextid = models.BigIntegerField()
    showinsubcontexts = models.IntegerField()
    pagetypepattern = models.CharField(max_length=64)
    subpagepattern = models.CharField(max_length=16, blank=True)
    defaultregion = models.CharField(max_length=16)
    defaultweight = models.BigIntegerField()
    configdata = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_block_instances'

class MdlBlockPositions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockinstanceid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    pagetype = models.CharField(max_length=64)
    subpage = models.CharField(max_length=16)
    visible = models.IntegerField()
    region = models.CharField(max_length=16)
    weight = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_block_positions'

class MdlBlockRssClient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    title = models.TextField()
    preferredtitle = models.CharField(max_length=64)
    description = models.TextField()
    shared = models.IntegerField()
    url = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_block_rss_client'

class MdlBlogAssociation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    blogid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_blog_association'

class MdlBlogExternal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.TextField()
    filtertags = models.CharField(max_length=255, blank=True)
    failedlastsync = models.IntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    timefetched = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_blog_external'

class MdlBook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    numbering = models.IntegerField()
    customtitles = models.IntegerField()
    revision = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_book'

class MdlBookChapters(models.Model):
    id = models.BigIntegerField(primary_key=True)
    bookid = models.BigIntegerField()
    pagenum = models.BigIntegerField()
    subchapter = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    contentformat = models.IntegerField()
    hidden = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    importsrc = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_book_chapters'

class MdlCacheFilters(models.Model):
    id = models.BigIntegerField(primary_key=True)
    filter = models.CharField(max_length=32)
    version = models.BigIntegerField()
    md5key = models.CharField(max_length=32)
    rawtext = models.TextField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_cache_filters'

class MdlCacheFlags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    flagtype = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    value = models.TextField()
    expiry = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_cache_flags'

class MdlCacheText(models.Model):
    id = models.BigIntegerField(primary_key=True)
    md5key = models.CharField(max_length=32)
    formattedtext = models.TextField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_cache_text'

class MdlCapabilities(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    captype = models.CharField(max_length=50)
    contextlevel = models.BigIntegerField()
    component = models.CharField(max_length=100)
    riskbitmask = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_capabilities'

class MdlChat(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    keepdays = models.BigIntegerField()
    studentlogs = models.IntegerField()
    chattime = models.BigIntegerField()
    schedule = models.IntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_chat'

class MdlChatMessages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.IntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_chat_messages'

class MdlChatMessagesCurrent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.IntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_chat_messages_current'

class MdlChatUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    version = models.CharField(max_length=16)
    ip = models.CharField(max_length=45)
    firstping = models.BigIntegerField()
    lastping = models.BigIntegerField()
    lastmessageping = models.BigIntegerField()
    sid = models.CharField(max_length=32)
    course = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_chat_users'

class MdlChoice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    publish = models.IntegerField()
    showresults = models.IntegerField()
    display = models.IntegerField()
    allowupdate = models.IntegerField()
    showunanswered = models.IntegerField()
    limitanswers = models.IntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_choice'

class MdlChoiceAnswers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    choiceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    optionid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_choice_answers'

class MdlChoiceOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    choiceid = models.BigIntegerField()
    text = models.TextField(blank=True)
    maxanswers = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_choice_options'

class MdlCohort(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=254)
    idnumber = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    component = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_cohort'

class MdlCohortMembers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cohortid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_cohort_members'

class MdlComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    commentarea = models.CharField(max_length=255)
    itemid = models.BigIntegerField()
    content = models.TextField()
    format = models.IntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_comments'

class MdlConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_config'

class MdlConfigLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True)
    oldvalue = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_config_log'

class MdlConfigPlugins(models.Model):
    id = models.BigIntegerField(primary_key=True)
    plugin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_config_plugins'

class MdlContext(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextlevel = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True)
    depth = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_context'

class MdlContextTemp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    path = models.CharField(max_length=255)
    depth = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_context_temp'

class MdlCourse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    sectioncache = models.TextField(blank=True)
    modinfo = models.TextField(blank=True)
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.IntegerField()
    showreports = models.IntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.IntegerField()
    groupmodeforce = models.IntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_course'

class MdlCourseCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    coursecount = models.BigIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    timemodified = models.BigIntegerField()
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_categories'

class MdlCourseCompletionAggrMethd(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_completion_aggr_methd'

class MdlCourseCompletionCritCompl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    criteriaid = models.BigIntegerField()
    gradefinal = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    unenroled = models.BigIntegerField(blank=True, null=True)
    timecompleted = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_completion_crit_compl'

class MdlCourseCompletionCriteria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField()
    module = models.CharField(max_length=100, blank=True)
    moduleinstance = models.BigIntegerField(blank=True, null=True)
    courseinstance = models.BigIntegerField(blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    timeend = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    role = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_completion_criteria'

class MdlCourseCompletions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    timeenrolled = models.BigIntegerField()
    timestarted = models.BigIntegerField()
    timecompleted = models.BigIntegerField(blank=True, null=True)
    reaggregate = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_course_completions'

class MdlCourseFormatOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    format = models.CharField(max_length=21)
    sectionid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_format_options'

class MdlCourseModules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    module = models.BigIntegerField()
    instance = models.BigIntegerField()
    section = models.BigIntegerField()
    idnumber = models.CharField(max_length=100, blank=True)
    added = models.BigIntegerField()
    score = models.IntegerField()
    indent = models.IntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.IntegerField()
    groupingid = models.BigIntegerField()
    groupmembersonly = models.IntegerField()
    completion = models.IntegerField()
    completiongradeitemnumber = models.BigIntegerField(blank=True, null=True)
    completionview = models.IntegerField()
    completionexpected = models.BigIntegerField()
    availablefrom = models.BigIntegerField()
    availableuntil = models.BigIntegerField()
    showavailability = models.IntegerField()
    showdescription = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_course_modules'

class MdlCourseModulesAvailFields(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    userfield = models.CharField(max_length=50, blank=True)
    customfieldid = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=20)
    value = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_course_modules_avail_fields'

class MdlCourseModulesAvailability(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    sourcecmid = models.BigIntegerField(blank=True, null=True)
    requiredcompletion = models.IntegerField(blank=True, null=True)
    gradeitemid = models.BigIntegerField(blank=True, null=True)
    grademin = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    grademax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_modules_availability'

class MdlCourseModulesCompletion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    completionstate = models.IntegerField()
    viewed = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_course_modules_completion'

class MdlCoursePublished(models.Model):
    id = models.BigIntegerField(primary_key=True)
    huburl = models.CharField(max_length=255, blank=True)
    courseid = models.BigIntegerField()
    timepublished = models.BigIntegerField()
    enrollable = models.IntegerField()
    hubcourseid = models.BigIntegerField()
    status = models.IntegerField(blank=True, null=True)
    timechecked = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_published'

class MdlCourseRequest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.IntegerField()
    category = models.BigIntegerField()
    reason = models.TextField()
    requester = models.BigIntegerField()
    password = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'mdl_course_request'

class MdlCourseSections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    section = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)
    summaryformat = models.IntegerField()
    sequence = models.TextField(blank=True)
    visible = models.IntegerField()
    availablefrom = models.BigIntegerField()
    availableuntil = models.BigIntegerField()
    showavailability = models.IntegerField()
    groupingid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_course_sections'

class MdlCourseSectionsAvailFields(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coursesectionid = models.BigIntegerField()
    userfield = models.CharField(max_length=50, blank=True)
    customfieldid = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=20)
    value = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_course_sections_avail_fields'

class MdlCourseSectionsAvailability(models.Model):
    id = models.BigIntegerField(primary_key=True)
    coursesectionid = models.BigIntegerField()
    sourcecmid = models.BigIntegerField(blank=True, null=True)
    requiredcompletion = models.IntegerField(blank=True, null=True)
    gradeitemid = models.BigIntegerField(blank=True, null=True)
    grademin = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    grademax = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_course_sections_availability'

class MdlData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    comments = models.IntegerField()
    timeavailablefrom = models.BigIntegerField()
    timeavailableto = models.BigIntegerField()
    timeviewfrom = models.BigIntegerField()
    timeviewto = models.BigIntegerField()
    requiredentries = models.IntegerField()
    requiredentriestoview = models.IntegerField()
    maxentries = models.IntegerField()
    rssarticles = models.IntegerField()
    singletemplate = models.TextField(blank=True)
    listtemplate = models.TextField(blank=True)
    listtemplateheader = models.TextField(blank=True)
    listtemplatefooter = models.TextField(blank=True)
    addtemplate = models.TextField(blank=True)
    rsstemplate = models.TextField(blank=True)
    rsstitletemplate = models.TextField(blank=True)
    csstemplate = models.TextField(blank=True)
    jstemplate = models.TextField(blank=True)
    asearchtemplate = models.TextField(blank=True)
    approval = models.IntegerField()
    scale = models.BigIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    defaultsort = models.BigIntegerField()
    defaultsortdir = models.IntegerField()
    editany = models.IntegerField()
    notification = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_data'

class MdlDataContent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fieldid = models.BigIntegerField()
    recordid = models.BigIntegerField()
    content = models.TextField(blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_data_content'

class MdlDataFields(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dataid = models.BigIntegerField()
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    param1 = models.TextField(blank=True)
    param2 = models.TextField(blank=True)
    param3 = models.TextField(blank=True)
    param4 = models.TextField(blank=True)
    param5 = models.TextField(blank=True)
    param6 = models.TextField(blank=True)
    param7 = models.TextField(blank=True)
    param8 = models.TextField(blank=True)
    param9 = models.TextField(blank=True)
    param10 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_data_fields'

class MdlDataRecords(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    dataid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    approved = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_data_records'

class MdlEnrol(models.Model):
    id = models.BigIntegerField(primary_key=True)
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    enrolstartdate = models.BigIntegerField(blank=True, null=True)
    enrolenddate = models.BigIntegerField(blank=True, null=True)
    expirynotify = models.IntegerField(blank=True, null=True)
    expirythreshold = models.BigIntegerField(blank=True, null=True)
    notifyall = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True)
    cost = models.CharField(max_length=20, blank=True)
    currency = models.CharField(max_length=3, blank=True)
    roleid = models.BigIntegerField(blank=True, null=True)
    customint1 = models.BigIntegerField(blank=True, null=True)
    customint2 = models.BigIntegerField(blank=True, null=True)
    customint3 = models.BigIntegerField(blank=True, null=True)
    customint4 = models.BigIntegerField(blank=True, null=True)
    customint5 = models.BigIntegerField(blank=True, null=True)
    customint6 = models.BigIntegerField(blank=True, null=True)
    customint7 = models.BigIntegerField(blank=True, null=True)
    customint8 = models.BigIntegerField(blank=True, null=True)
    customchar1 = models.CharField(max_length=255, blank=True)
    customchar2 = models.CharField(max_length=255, blank=True)
    customchar3 = models.CharField(max_length=1333, blank=True)
    customdec1 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customdec2 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customtext1 = models.TextField(blank=True)
    customtext2 = models.TextField(blank=True)
    customtext3 = models.TextField(blank=True)
    customtext4 = models.TextField(blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_enrol'

class MdlEnrolAuthorize(models.Model):
    id = models.BigIntegerField(primary_key=True)
    paymentmethod = models.CharField(max_length=6)
    refundinfo = models.IntegerField()
    ccname = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    transid = models.BigIntegerField()
    status = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    settletime = models.BigIntegerField()
    amount = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    class Meta:
        managed = False
        db_table = 'mdl_enrol_authorize'

class MdlEnrolAuthorizeRefunds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    orderid = models.BigIntegerField()
    status = models.IntegerField()
    amount = models.CharField(max_length=10)
    transid = models.BigIntegerField(blank=True, null=True)
    settletime = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_enrol_authorize_refunds'

class MdlEnrolFlatfile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.CharField(max_length=30)
    roleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_enrol_flatfile'

class MdlEnrolPaypal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    business = models.CharField(max_length=255)
    receiver_email = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    memo = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)
    option_name1 = models.CharField(max_length=255)
    option_selection1_x = models.CharField(max_length=255)
    option_name2 = models.CharField(max_length=255)
    option_selection2_x = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    reason_code = models.CharField(max_length=30)
    txn_id = models.CharField(max_length=255)
    parent_txn_id = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=30)
    timeupdated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_enrol_paypal'

class MdlEvent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    format = models.IntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    repeatid = models.BigIntegerField()
    modulename = models.CharField(max_length=20)
    instance = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    timestart = models.BigIntegerField()
    timeduration = models.BigIntegerField()
    visible = models.IntegerField()
    uuid = models.CharField(max_length=255)
    sequence = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    subscriptionid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_event'

class MdlEventSubscriptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    pollinterval = models.BigIntegerField()
    lastupdated = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_event_subscriptions'

class MdlEventsHandlers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    eventname = models.CharField(max_length=166)
    component = models.CharField(max_length=166)
    handlerfile = models.CharField(max_length=255)
    handlerfunction = models.TextField(blank=True)
    schedule = models.CharField(max_length=255, blank=True)
    status = models.BigIntegerField()
    internal = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_events_handlers'

class MdlEventsQueue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    eventdata = models.TextField()
    stackdump = models.TextField(blank=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_events_queue'

class MdlEventsQueueHandlers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    queuedeventid = models.BigIntegerField()
    handlerid = models.BigIntegerField()
    status = models.BigIntegerField(blank=True, null=True)
    errormessage = models.TextField(blank=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_events_queue_handlers'

class MdlExternalFunctions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    classname = models.CharField(max_length=100)
    methodname = models.CharField(max_length=100)
    classpath = models.CharField(max_length=255, blank=True)
    component = models.CharField(max_length=100)
    capabilities = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_external_functions'

class MdlExternalServices(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    enabled = models.IntegerField()
    requiredcapability = models.CharField(max_length=150, blank=True)
    restrictedusers = models.IntegerField()
    component = models.CharField(max_length=100, blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True)
    downloadfiles = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_external_services'

class MdlExternalServicesFunctions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    functionname = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'mdl_external_services_functions'

class MdlExternalServicesUsers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_external_services_users'

class MdlExternalTokens(models.Model):
    id = models.BigIntegerField(primary_key=True)
    token = models.CharField(max_length=128)
    tokentype = models.IntegerField()
    userid = models.BigIntegerField()
    externalserviceid = models.BigIntegerField()
    sid = models.CharField(max_length=128, blank=True)
    contextid = models.BigIntegerField()
    creatorid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    lastaccess = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_external_tokens'

class MdlFeedback(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    anonymous = models.IntegerField()
    email_notification = models.IntegerField()
    multiple_submit = models.IntegerField()
    autonumbering = models.IntegerField()
    site_after_submit = models.CharField(max_length=255)
    page_after_submit = models.TextField()
    page_after_submitformat = models.IntegerField()
    publish_stats = models.IntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback'

class MdlFeedbackCompleted(models.Model):
    id = models.BigIntegerField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_completed'

class MdlFeedbackCompletedtmp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    guestid = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_completedtmp'

class MdlFeedbackItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    feedback = models.BigIntegerField()
    template = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    presentation = models.TextField()
    typ = models.CharField(max_length=255)
    hasvalue = models.IntegerField()
    position = models.IntegerField()
    required = models.IntegerField()
    dependitem = models.BigIntegerField()
    dependvalue = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_feedback_item'

class MdlFeedbackSitecourseMap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    feedbackid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_sitecourse_map'

class MdlFeedbackTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    ispublic = models.IntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_feedback_template'

class MdlFeedbackTracking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    feedback = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_tracking'

class MdlFeedbackValue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_value'

class MdlFeedbackValuetmp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_feedback_valuetmp'

class MdlFiles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contenthash = models.CharField(max_length=40)
    pathnamehash = models.CharField(unique=True, max_length=40)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    filearea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    filepath = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    userid = models.BigIntegerField(blank=True, null=True)
    filesize = models.BigIntegerField()
    mimetype = models.CharField(max_length=100, blank=True)
    status = models.BigIntegerField()
    source = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    license = models.CharField(max_length=255, blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    referencefileid = models.BigIntegerField(blank=True, null=True)
    referencelastsync = models.BigIntegerField(blank=True, null=True)
    referencelifetime = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_files'

class MdlFilesReference(models.Model):
    id = models.BigIntegerField(primary_key=True)
    repositoryid = models.BigIntegerField()
    lastsync = models.BigIntegerField(blank=True, null=True)
    lifetime = models.BigIntegerField(blank=True, null=True)
    reference = models.TextField(blank=True)
    referencehash = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'mdl_files_reference'

class MdlFilterActive(models.Model):
    id = models.BigIntegerField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    active = models.IntegerField()
    sortorder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_filter_active'

class MdlFilterConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_filter_config'

class MdlFolder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    display = models.IntegerField()
    showexpanded = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_folder'

class MdlForum(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    maxattachments = models.BigIntegerField()
    forcesubscribe = models.IntegerField()
    trackingtype = models.IntegerField()
    rsstype = models.IntegerField()
    rssarticles = models.IntegerField()
    timemodified = models.BigIntegerField()
    warnafter = models.BigIntegerField()
    blockafter = models.BigIntegerField()
    blockperiod = models.BigIntegerField()
    completiondiscussions = models.IntegerField()
    completionreplies = models.IntegerField()
    completionposts = models.IntegerField()
    displaywordcount = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum'

class MdlForumDiscussions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    forum = models.BigIntegerField()
    name = models.CharField(max_length=255)
    firstpost = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    assessed = models.IntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_discussions'

class MdlForumPosts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    discussion = models.BigIntegerField()
    parent = models.BigIntegerField()
    userid = models.BigIntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    mailed = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    messageformat = models.IntegerField()
    messagetrust = models.IntegerField()
    attachment = models.CharField(max_length=100)
    totalscore = models.IntegerField()
    mailnow = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_posts'

class MdlForumQueue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_queue'

class MdlForumRead(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    firstread = models.BigIntegerField()
    lastread = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_read'

class MdlForumSubscriptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    forum = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_subscriptions'

class MdlForumTrackPrefs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_forum_track_prefs'

class MdlGlossary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    allowduplicatedentries = models.IntegerField()
    displayformat = models.CharField(max_length=50)
    mainglossary = models.IntegerField()
    showspecial = models.IntegerField()
    showalphabet = models.IntegerField()
    showall = models.IntegerField()
    allowcomments = models.IntegerField()
    allowprintview = models.IntegerField()
    usedynalink = models.IntegerField()
    defaultapproval = models.IntegerField()
    approvaldisplayformat = models.CharField(max_length=50)
    globalglossary = models.IntegerField()
    entbypage = models.IntegerField()
    editalways = models.IntegerField()
    rsstype = models.IntegerField()
    rssarticles = models.IntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionentries = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_glossary'

class MdlGlossaryAlias(models.Model):
    id = models.BigIntegerField(primary_key=True)
    entryid = models.BigIntegerField()
    alias = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_glossary_alias'

class MdlGlossaryCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    glossaryid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    usedynalink = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_glossary_categories'

class MdlGlossaryEntries(models.Model):
    id = models.BigIntegerField(primary_key=True)
    glossaryid = models.BigIntegerField()
    userid = models.BigIntegerField()
    concept = models.CharField(max_length=255)
    definition = models.TextField()
    definitionformat = models.IntegerField()
    definitiontrust = models.IntegerField()
    attachment = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    teacherentry = models.IntegerField()
    sourceglossaryid = models.BigIntegerField()
    usedynalink = models.IntegerField()
    casesensitive = models.IntegerField()
    fullmatch = models.IntegerField()
    approved = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_glossary_entries'

class MdlGlossaryEntriesCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    categoryid = models.BigIntegerField()
    entryid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_glossary_entries_categories'

class MdlGlossaryFormats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    popupformatname = models.CharField(max_length=50)
    visible = models.IntegerField()
    showgroup = models.IntegerField()
    defaultmode = models.CharField(max_length=50)
    defaulthook = models.CharField(max_length=50)
    sortkey = models.CharField(max_length=50)
    sortorder = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'mdl_glossary_formats'

class MdlGradeCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.IntegerField()
    aggregateoutcomes = models.IntegerField()
    aggregatesubcats = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    hidden = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_categories'

class MdlGradeCategoriesHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.IntegerField()
    aggregateoutcomes = models.IntegerField()
    aggregatesubcats = models.IntegerField()
    hidden = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_categories_history'

class MdlGradeGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True)
    informationformat = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_grades'

class MdlGradeGradesHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True)
    informationformat = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_grades_history'

class MdlGradeImportNewitem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemname = models.CharField(max_length=255)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_import_newitem'

class MdlGradeImportValues(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.BigIntegerField(blank=True, null=True)
    newgradeitem = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField()
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    feedback = models.TextField(blank=True)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_import_values'

class MdlGradeItems(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True)
    idnumber = models.CharField(max_length=255, blank=True)
    calculation = models.TextField(blank=True)
    gradetype = models.IntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.IntegerField(blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_items'

class MdlGradeItemsHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True)
    idnumber = models.CharField(max_length=255, blank=True)
    calculation = models.TextField(blank=True)
    gradetype = models.IntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_items_history'

class MdlGradeLetters(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    lowerboundary = models.DecimalField(max_digits=10, decimal_places=5)
    letter = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_grade_letters'

class MdlGradeOutcomes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes'

class MdlGradeOutcomesCourses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    outcomeid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes_courses'

class MdlGradeOutcomesHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grade_outcomes_history'

class MdlGradeSettings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_grade_settings'

class MdlGradingAreas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    areaname = models.CharField(max_length=100)
    activemethod = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_grading_areas'

class MdlGradingDefinitions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    areaid = models.BigIntegerField()
    method = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    status = models.BigIntegerField()
    copiedfromid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timecopied = models.BigIntegerField(blank=True, null=True)
    options = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_grading_definitions'

class MdlGradingInstances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    definitionid = models.BigIntegerField()
    raterid = models.BigIntegerField()
    itemid = models.BigIntegerField(blank=True, null=True)
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    status = models.BigIntegerField()
    feedback = models.TextField(blank=True)
    feedbackformat = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_grading_instances'

class MdlGradingformGuideComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_comments'

class MdlGradingformGuideCriteria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    shortname = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    descriptionmarkers = models.TextField(blank=True)
    descriptionmarkersformat = models.IntegerField(blank=True, null=True)
    maxscore = models.DecimalField(max_digits=10, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_criteria'

class MdlGradingformGuideFillings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    remark = models.TextField(blank=True)
    remarkformat = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_guide_fillings'

class MdlGradingformRubricCriteria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_criteria'

class MdlGradingformRubricFillings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    levelid = models.BigIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True)
    remarkformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_fillings'

class MdlGradingformRubricLevels(models.Model):
    id = models.BigIntegerField(primary_key=True)
    criterionid = models.BigIntegerField()
    score = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True)
    definitionformat = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_gradingform_rubric_levels'

class MdlGroupings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    configdata = models.TextField(blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_groupings'

class MdlGroupingsGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    groupingid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    timeadded = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_groupings_groups'

class MdlGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    idnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    enrolmentkey = models.CharField(max_length=50, blank=True)
    picture = models.BigIntegerField()
    hidepicture = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_groups'

class MdlGroupsMembers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_groups_members'

class MdlImscp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    revision = models.BigIntegerField()
    keepold = models.BigIntegerField()
    structure = models.TextField(blank=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_imscp'

class MdlLabel(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_label'

class MdlLesson(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    practice = models.IntegerField()
    modattempts = models.IntegerField()
    usepassword = models.IntegerField()
    password = models.CharField(max_length=32)
    dependency = models.BigIntegerField()
    conditions = models.TextField()
    grade = models.IntegerField()
    custom = models.IntegerField()
    ongoing = models.IntegerField()
    usemaxgrade = models.IntegerField()
    maxanswers = models.IntegerField()
    maxattempts = models.IntegerField()
    review = models.IntegerField()
    nextpagedefault = models.IntegerField()
    feedback = models.IntegerField()
    minquestions = models.IntegerField()
    maxpages = models.IntegerField()
    timed = models.IntegerField()
    maxtime = models.BigIntegerField()
    retake = models.IntegerField()
    activitylink = models.BigIntegerField()
    mediafile = models.CharField(max_length=255)
    mediaheight = models.BigIntegerField()
    mediawidth = models.BigIntegerField()
    mediaclose = models.IntegerField()
    slideshow = models.IntegerField()
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    bgcolor = models.CharField(max_length=7)
    displayleft = models.IntegerField()
    displayleftif = models.IntegerField()
    progressbar = models.IntegerField()
    highscores = models.IntegerField()
    maxhighscores = models.BigIntegerField()
    available = models.BigIntegerField()
    deadline = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson'

class MdlLessonAnswers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    jumpto = models.BigIntegerField()
    grade = models.IntegerField()
    score = models.BigIntegerField()
    flags = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    answer = models.TextField(blank=True)
    answerformat = models.IntegerField()
    response = models.TextField(blank=True)
    responseformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_answers'

class MdlLessonAttempts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    userid = models.BigIntegerField()
    answerid = models.BigIntegerField()
    retry = models.IntegerField()
    correct = models.BigIntegerField()
    useranswer = models.TextField(blank=True)
    timeseen = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_attempts'

class MdlLessonBranch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    retry = models.BigIntegerField()
    flag = models.IntegerField()
    timeseen = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_branch'

class MdlLessonGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.FloatField()
    late = models.IntegerField()
    completed = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_grades'

class MdlLessonHighScores(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    gradeid = models.BigIntegerField()
    nickname = models.CharField(max_length=5)
    class Meta:
        managed = False
        db_table = 'mdl_lesson_high_scores'

class MdlLessonPages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    prevpageid = models.BigIntegerField()
    nextpageid = models.BigIntegerField()
    qtype = models.IntegerField()
    qoption = models.IntegerField()
    layout = models.IntegerField()
    display = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    contents = models.TextField()
    contentsformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_pages'

class MdlLessonTimer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    starttime = models.BigIntegerField()
    lessontime = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lesson_timer'

class MdlLicense(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shortname = models.CharField(max_length=255, blank=True)
    fullname = models.TextField(blank=True)
    source = models.CharField(max_length=255, blank=True)
    enabled = models.IntegerField()
    version = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_license'

class MdlLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_log'

class MdlLogDisplay(models.Model):
    id = models.BigIntegerField(primary_key=True)
    module = models.CharField(max_length=20)
    action = models.CharField(max_length=40)
    mtable = models.CharField(max_length=30)
    field = models.CharField(max_length=200)
    component = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'mdl_log_display'

class MdlLogQueries(models.Model):
    id = models.BigIntegerField(primary_key=True)
    qtype = models.IntegerField()
    sqltext = models.TextField()
    sqlparams = models.TextField(blank=True)
    error = models.IntegerField()
    info = models.TextField(blank=True)
    backtrace = models.TextField(blank=True)
    exectime = models.DecimalField(max_digits=10, decimal_places=5)
    timelogged = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_log_queries'

class MdlLti(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    typeid = models.BigIntegerField(blank=True, null=True)
    toolurl = models.TextField()
    securetoolurl = models.TextField(blank=True)
    instructorchoicesendname = models.IntegerField(blank=True, null=True)
    instructorchoicesendemailaddr = models.IntegerField(blank=True, null=True)
    instructorchoiceallowroster = models.IntegerField(blank=True, null=True)
    instructorchoiceallowsetting = models.IntegerField(blank=True, null=True)
    instructorcustomparameters = models.CharField(max_length=255, blank=True)
    instructorchoiceacceptgrades = models.IntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    launchcontainer = models.IntegerField()
    resourcekey = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    debuglaunch = models.IntegerField()
    showtitlelaunch = models.IntegerField()
    showdescriptionlaunch = models.IntegerField()
    servicesalt = models.CharField(max_length=40, blank=True)
    icon = models.TextField(blank=True)
    secureicon = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_lti'

class MdlLtiSubmission(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ltiid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datesubmitted = models.BigIntegerField()
    dateupdated = models.BigIntegerField()
    gradepercent = models.DecimalField(max_digits=10, decimal_places=5)
    originalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    launchid = models.BigIntegerField()
    state = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lti_submission'

class MdlLtiTypes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    baseurl = models.TextField()
    tooldomain = models.CharField(max_length=255)
    state = models.IntegerField()
    course = models.BigIntegerField()
    coursevisible = models.IntegerField()
    createdby = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_lti_types'

class MdlLtiTypesConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    typeid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_lti_types_config'

class MdlMessage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True)
    fullmessage = models.TextField(blank=True)
    fullmessageformat = models.IntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True)
    smallmessage = models.TextField(blank=True)
    notification = models.IntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True)
    contexturlname = models.TextField(blank=True)
    timecreated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_message'

class MdlMessageContacts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    contactid = models.BigIntegerField()
    blocked = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_message_contacts'

class MdlMessageProcessors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=166)
    enabled = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_message_processors'

class MdlMessageProviders(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    component = models.CharField(max_length=200)
    capability = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_message_providers'

class MdlMessageRead(models.Model):
    id = models.BigIntegerField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True)
    fullmessage = models.TextField(blank=True)
    fullmessageformat = models.IntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True)
    smallmessage = models.TextField(blank=True)
    notification = models.IntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True)
    contexturlname = models.TextField(blank=True)
    timecreated = models.BigIntegerField()
    timeread = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_message_read'

class MdlMessageWorking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    unreadmessageid = models.BigIntegerField()
    processorid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_message_working'

class MdlMnetApplication(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    xmlrpc_server_url = models.CharField(max_length=255)
    sso_land_url = models.CharField(max_length=255)
    sso_jump_url = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_mnet_application'

class MdlMnetHost(models.Model):
    id = models.BigIntegerField(primary_key=True)
    deleted = models.IntegerField()
    wwwroot = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=45)
    name = models.CharField(max_length=80)
    public_key = models.TextField()
    public_key_expires = models.BigIntegerField()
    transport = models.IntegerField()
    portno = models.IntegerField()
    last_connect_time = models.BigIntegerField()
    last_log_id = models.BigIntegerField()
    force_theme = models.IntegerField()
    theme = models.CharField(max_length=100, blank=True)
    applicationid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_host'

class MdlMnetHost2Service(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hostid = models.BigIntegerField()
    serviceid = models.BigIntegerField()
    publish = models.IntegerField()
    subscribe = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_host2service'

class MdlMnetLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    coursename = models.CharField(max_length=40)
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_mnet_log'

class MdlMnetRemoteRpc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_remote_rpc'

class MdlMnetRemoteService2Rpc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_remote_service2rpc'

class MdlMnetRpc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.IntegerField()
    help = models.TextField()
    profile = models.TextField()
    filename = models.CharField(max_length=100)
    classname = models.CharField(max_length=150, blank=True)
    static = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_mnet_rpc'

class MdlMnetService(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    apiversion = models.CharField(max_length=10)
    offer = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_service'

class MdlMnetService2Rpc(models.Model):
    id = models.BigIntegerField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_service2rpc'

class MdlMnetSession(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    token = models.CharField(unique=True, max_length=40)
    mnethostid = models.BigIntegerField()
    useragent = models.CharField(max_length=40)
    confirm_timeout = models.BigIntegerField()
    session_id = models.CharField(max_length=40)
    expires = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_mnet_session'

class MdlMnetSsoAccessControl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    mnet_host_id = models.BigIntegerField()
    accessctrl = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'mdl_mnet_sso_access_control'

class MdlMnetserviceEnrolCourses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    categoryid = models.BigIntegerField()
    categoryname = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.IntegerField(blank=True, null=True)
    startdate = models.BigIntegerField()
    roleid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_mnetservice_enrol_courses'

class MdlMnetserviceEnrolEnrolments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hostid = models.BigIntegerField()
    userid = models.BigIntegerField()
    remotecourseid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)
    enroltime = models.BigIntegerField()
    enroltype = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'mdl_mnetservice_enrol_enrolments'

class MdlModules(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    version = models.BigIntegerField()
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    search = models.CharField(max_length=255)
    visible = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_modules'

class MdlMyPages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    private = models.IntegerField()
    sortorder = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_my_pages'

class MdlPage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    content = models.TextField(blank=True)
    contentformat = models.IntegerField()
    legacyfiles = models.IntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.IntegerField()
    displayoptions = models.TextField(blank=True)
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_page'

class MdlPortfolioInstance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    plugin = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    visible = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance'

class MdlPortfolioInstanceConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instance = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance_config'

class MdlPortfolioInstanceUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instance = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_instance_user'

class MdlPortfolioLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    time = models.BigIntegerField()
    portfolio = models.BigIntegerField()
    caller_class = models.CharField(max_length=150)
    caller_file = models.CharField(max_length=255)
    caller_component = models.CharField(max_length=255, blank=True)
    caller_sha1 = models.CharField(max_length=255)
    tempdataid = models.BigIntegerField()
    returnurl = models.CharField(max_length=255)
    continueurl = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_log'

class MdlPortfolioMaharaQueue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    transferid = models.BigIntegerField()
    token = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_mahara_queue'

class MdlPortfolioTempdata(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.TextField(blank=True)
    expirytime = models.BigIntegerField()
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_portfolio_tempdata'

class MdlPost(models.Model):
    id = models.BigIntegerField(primary_key=True)
    module = models.CharField(max_length=20)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    moduleid = models.BigIntegerField()
    coursemoduleid = models.BigIntegerField()
    subject = models.CharField(max_length=128)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    uniquehash = models.CharField(max_length=255)
    rating = models.BigIntegerField()
    format = models.BigIntegerField()
    summaryformat = models.IntegerField()
    attachment = models.CharField(max_length=100, blank=True)
    publishstate = models.CharField(max_length=20)
    lastmodified = models.BigIntegerField()
    created = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_post'

class MdlProfiling(models.Model):
    id = models.BigIntegerField(primary_key=True)
    runid = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=255)
    data = models.TextField()
    totalexecutiontime = models.BigIntegerField()
    totalcputime = models.BigIntegerField()
    totalcalls = models.BigIntegerField()
    totalmemory = models.BigIntegerField()
    runreference = models.IntegerField()
    runcomment = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_profiling'

class MdlQtypeEssayOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    responseformat = models.CharField(max_length=16)
    responsefieldlines = models.IntegerField()
    attachments = models.IntegerField()
    graderinfo = models.TextField(blank=True)
    graderinfoformat = models.IntegerField()
    responsetemplate = models.TextField(blank=True)
    responsetemplateformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_qtype_essay_options'

class MdlQtypeMatchOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    shuffleanswers = models.IntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.IntegerField()
    shownumcorrect = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_qtype_match_options'

class MdlQtypeMatchSubquestions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionid = models.BigIntegerField()
    questiontext = models.TextField()
    questiontextformat = models.IntegerField()
    answertext = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_qtype_match_subquestions'

class MdlQtypeShortanswerOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    usecase = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_qtype_shortanswer_options'

class MdlQuestion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category = models.BigIntegerField()
    parent = models.BigIntegerField()
    name = models.CharField(max_length=255)
    questiontext = models.TextField()
    questiontextformat = models.IntegerField()
    generalfeedback = models.TextField()
    generalfeedbackformat = models.IntegerField()
    defaultmark = models.DecimalField(max_digits=12, decimal_places=7)
    penalty = models.DecimalField(max_digits=12, decimal_places=7)
    qtype = models.CharField(max_length=20)
    length = models.BigIntegerField()
    stamp = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    hidden = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_question'

class MdlQuestionAnswers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.TextField()
    answerformat = models.IntegerField()
    fraction = models.DecimalField(max_digits=12, decimal_places=7)
    feedback = models.TextField()
    feedbackformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_answers'

class MdlQuestionAttemptStepData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attemptstepid = models.BigIntegerField()
    name = models.CharField(max_length=32)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_question_attempt_step_data'

class MdlQuestionAttemptSteps(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionattemptid = models.BigIntegerField()
    sequencenumber = models.BigIntegerField()
    state = models.CharField(max_length=13)
    fraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_question_attempt_steps'

class MdlQuestionAttempts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    behaviour = models.CharField(max_length=32)
    questionid = models.BigIntegerField()
    variant = models.BigIntegerField()
    maxmark = models.DecimalField(max_digits=12, decimal_places=7)
    minfraction = models.DecimalField(max_digits=12, decimal_places=7)
    flagged = models.IntegerField()
    questionsummary = models.TextField(blank=True)
    rightanswer = models.TextField(blank=True)
    responsesummary = models.TextField(blank=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_attempts'

class MdlQuestionCalculated(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=20)
    tolerancetype = models.BigIntegerField()
    correctanswerlength = models.BigIntegerField()
    correctanswerformat = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_calculated'

class MdlQuestionCalculatedOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    synchronize = models.IntegerField()
    single = models.IntegerField()
    shuffleanswers = models.IntegerField()
    correctfeedback = models.TextField(blank=True)
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField(blank=True)
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField(blank=True)
    incorrectfeedbackformat = models.IntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_calculated_options'

class MdlQuestionCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    contextid = models.BigIntegerField()
    info = models.TextField()
    infoformat = models.IntegerField()
    stamp = models.CharField(max_length=255)
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_categories'

class MdlQuestionDatasetDefinitions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.BigIntegerField()
    options = models.CharField(max_length=255)
    itemcount = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_dataset_definitions'

class MdlQuestionDatasetItems(models.Model):
    id = models.BigIntegerField(primary_key=True)
    definition = models.BigIntegerField()
    itemnumber = models.BigIntegerField()
    value = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_question_dataset_items'

class MdlQuestionDatasets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    datasetdefinition = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_datasets'

class MdlQuestionHints(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionid = models.BigIntegerField()
    hint = models.TextField()
    hintformat = models.IntegerField()
    shownumcorrect = models.IntegerField(blank=True, null=True)
    clearwrong = models.IntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_question_hints'

class MdlQuestionMultianswer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    sequence = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_question_multianswer'

class MdlQuestionMultichoice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    layout = models.IntegerField()
    answers = models.CharField(max_length=255)
    single = models.IntegerField()
    shuffleanswers = models.IntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.IntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_multichoice'

class MdlQuestionNumerical(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_question_numerical'

class MdlQuestionNumericalOptions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    showunits = models.IntegerField()
    unitsleft = models.IntegerField()
    unitgradingtype = models.IntegerField()
    unitpenalty = models.DecimalField(max_digits=12, decimal_places=7)
    class Meta:
        managed = False
        db_table = 'mdl_question_numerical_options'

class MdlQuestionNumericalUnits(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    multiplier = models.DecimalField(max_digits=40, decimal_places=20)
    unit = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'mdl_question_numerical_units'

class MdlQuestionRandomsamatch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    choose = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_randomsamatch'

class MdlQuestionSessions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attemptid = models.BigIntegerField()
    questionid = models.BigIntegerField()
    newest = models.BigIntegerField()
    newgraded = models.BigIntegerField()
    sumpenalty = models.DecimalField(max_digits=12, decimal_places=7)
    manualcomment = models.TextField()
    manualcommentformat = models.IntegerField()
    flagged = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_sessions'

class MdlQuestionStates(models.Model):
    id = models.BigIntegerField(primary_key=True)
    attempt = models.BigIntegerField()
    question = models.BigIntegerField()
    seq_number = models.IntegerField()
    answer = models.TextField()
    timestamp = models.BigIntegerField()
    event = models.IntegerField()
    grade = models.DecimalField(max_digits=12, decimal_places=7)
    raw_grade = models.DecimalField(max_digits=12, decimal_places=7)
    penalty = models.DecimalField(max_digits=12, decimal_places=7)
    class Meta:
        managed = False
        db_table = 'mdl_question_states'

class MdlQuestionTruefalse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.BigIntegerField()
    trueanswer = models.BigIntegerField()
    falseanswer = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_question_truefalse'

class MdlQuestionUsages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=255)
    preferredbehaviour = models.CharField(max_length=32)
    class Meta:
        managed = False
        db_table = 'mdl_question_usages'

class MdlQuiz(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timelimit = models.BigIntegerField()
    overduehandling = models.CharField(max_length=16)
    graceperiod = models.BigIntegerField()
    preferredbehaviour = models.CharField(max_length=32)
    attempts = models.IntegerField()
    attemptonlast = models.IntegerField()
    grademethod = models.IntegerField()
    decimalpoints = models.IntegerField()
    questiondecimalpoints = models.IntegerField()
    reviewattempt = models.IntegerField()
    reviewcorrectness = models.IntegerField()
    reviewmarks = models.IntegerField()
    reviewspecificfeedback = models.IntegerField()
    reviewgeneralfeedback = models.IntegerField()
    reviewrightanswer = models.IntegerField()
    reviewoverallfeedback = models.IntegerField()
    questionsperpage = models.BigIntegerField()
    navmethod = models.CharField(max_length=16)
    shufflequestions = models.IntegerField()
    shuffleanswers = models.IntegerField()
    questions = models.TextField()
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5)
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    password = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    browsersecurity = models.CharField(max_length=32)
    delay1 = models.BigIntegerField()
    delay2 = models.BigIntegerField()
    showuserpicture = models.IntegerField()
    showblocks = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_quiz'

class MdlQuizAttempts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    attempt = models.IntegerField()
    uniqueid = models.BigIntegerField(unique=True)
    layout = models.TextField()
    currentpage = models.BigIntegerField()
    preview = models.IntegerField()
    state = models.CharField(max_length=16)
    timestart = models.BigIntegerField()
    timefinish = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timecheckstate = models.BigIntegerField(blank=True, null=True)
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    needsupgradetonewqe = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_quiz_attempts'

class MdlQuizFeedback(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quizid = models.BigIntegerField()
    feedbacktext = models.TextField()
    feedbacktextformat = models.IntegerField()
    mingrade = models.DecimalField(max_digits=10, decimal_places=5)
    maxgrade = models.DecimalField(max_digits=10, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_feedback'

class MdlQuizGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_quiz_grades'

class MdlQuizOverrides(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quiz = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timeopen = models.BigIntegerField(blank=True, null=True)
    timeclose = models.BigIntegerField(blank=True, null=True)
    timelimit = models.BigIntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_overrides'

class MdlQuizOverviewRegrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    newfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    oldfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    regraded = models.IntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_quiz_overview_regrades'

class MdlQuizQuestionInstances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quiz = models.BigIntegerField()
    question = models.BigIntegerField()
    grade = models.DecimalField(max_digits=12, decimal_places=7)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_question_instances'

class MdlQuizQuestionResponseStats(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quizstatisticsid = models.BigIntegerField()
    questionid = models.BigIntegerField()
    subqid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100, blank=True)
    response = models.TextField(blank=True)
    rcount = models.BigIntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_question_response_stats'

class MdlQuizQuestionStatistics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quizstatisticsid = models.BigIntegerField()
    questionid = models.BigIntegerField()
    slot = models.BigIntegerField(blank=True, null=True)
    subquestion = models.IntegerField()
    s = models.BigIntegerField()
    effectiveweight = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    negcovar = models.IntegerField()
    discriminationindex = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    discriminativeefficiency = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    sd = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    facility = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    subquestions = models.TextField(blank=True)
    maxmark = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    positions = models.TextField(blank=True)
    randomguessscore = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_question_statistics'

class MdlQuizReports(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True)
    displayorder = models.BigIntegerField()
    capability = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_reports'

class MdlQuizStatistics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    quizid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    allattempts = models.IntegerField()
    timemodified = models.BigIntegerField()
    firstattemptscount = models.BigIntegerField()
    allattemptscount = models.BigIntegerField()
    firstattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    allattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    median = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    standarddeviation = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    skewness = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    kurtosis = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cic = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    errorratio = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    standarderror = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_quiz_statistics'

class MdlRating(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    ratingarea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    scaleid = models.BigIntegerField()
    rating = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_rating'

class MdlRegistrationHubs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    token = models.CharField(max_length=255)
    hubname = models.CharField(max_length=255)
    huburl = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    secret = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_registration_hubs'

class MdlRepository(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    visible = models.IntegerField(blank=True, null=True)
    sortorder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_repository'

class MdlRepositoryInstanceConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    instanceid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_repository_instance_config'

class MdlRepositoryInstances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    typeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    readonly = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_repository_instances'

class MdlResource(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    tobemigrated = models.IntegerField()
    legacyfiles = models.IntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.IntegerField()
    displayoptions = models.TextField(blank=True)
    filterfiles = models.IntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_resource'

class MdlResourceOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    reference = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    alltext = models.TextField()
    popup = models.TextField()
    options = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    oldid = models.BigIntegerField(unique=True)
    cmid = models.BigIntegerField(blank=True, null=True)
    newmodule = models.CharField(max_length=50, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    migrated = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_resource_old'

class MdlRole(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    shortname = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    sortorder = models.BigIntegerField(unique=True)
    archetype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_role'

class MdlRoleAllowAssign(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    allowassign = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_allow_assign'

class MdlRoleAllowOverride(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    allowoverride = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_allow_override'

class MdlRoleAllowSwitch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    allowswitch = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_allow_switch'

class MdlRoleAssignments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_assignments'

class MdlRoleCapabilities(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contextid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    capability = models.CharField(max_length=255)
    permission = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_capabilities'

class MdlRoleContextLevels(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_context_levels'

class MdlRoleNames(models.Model):
    id = models.BigIntegerField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_role_names'

class MdlRoleSortorder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    sortoder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_role_sortorder'

class MdlScale(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    descriptionformat = models.IntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_scale'

class MdlScaleHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_scale_history'

class MdlScorm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scormtype = models.CharField(max_length=50)
    reference = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    version = models.CharField(max_length=9)
    maxgrade = models.FloatField()
    grademethod = models.IntegerField()
    whatgrade = models.BigIntegerField()
    maxattempt = models.BigIntegerField()
    forcecompleted = models.IntegerField()
    forcenewattempt = models.IntegerField()
    lastattemptlock = models.IntegerField()
    displayattemptstatus = models.IntegerField()
    displaycoursestructure = models.IntegerField()
    updatefreq = models.IntegerField()
    sha1hash = models.CharField(max_length=40, blank=True)
    md5hash = models.CharField(max_length=32)
    revision = models.BigIntegerField()
    launch = models.BigIntegerField()
    skipview = models.IntegerField()
    hidebrowse = models.IntegerField()
    hidetoc = models.IntegerField()
    hidenav = models.IntegerField()
    auto = models.IntegerField()
    popup = models.IntegerField()
    options = models.CharField(max_length=255)
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionstatusrequired = models.IntegerField(blank=True, null=True)
    completionscorerequired = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_scorm'

class MdlScormAiccSession(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    hacpsession = models.CharField(max_length=255)
    scoid = models.BigIntegerField(blank=True, null=True)
    scormmode = models.CharField(max_length=50, blank=True)
    scormstatus = models.CharField(max_length=255, blank=True)
    attempt = models.BigIntegerField(blank=True, null=True)
    lessonstatus = models.CharField(max_length=255, blank=True)
    sessiontime = models.CharField(max_length=255, blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_scorm_aicc_session'

class MdlScormScoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scorm = models.BigIntegerField()
    manifest = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    launch = models.TextField()
    scormtype = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes'

class MdlScormScoesData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes_data'

class MdlScormScoesTrack(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    scoid = models.BigIntegerField()
    attempt = models.BigIntegerField()
    element = models.CharField(max_length=255)
    value = models.TextField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_scorm_scoes_track'

class MdlScormSeqMapinfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    objectiveid = models.BigIntegerField()
    targetobjectiveid = models.BigIntegerField()
    readsatisfiedstatus = models.IntegerField()
    readnormalizedmeasure = models.IntegerField()
    writesatisfiedstatus = models.IntegerField()
    writenormalizedmeasure = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_mapinfo'

class MdlScormSeqObjective(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    primaryobj = models.IntegerField()
    objectiveid = models.CharField(max_length=255)
    satisfiedbymeasure = models.IntegerField()
    minnormalizedmeasure = models.FloatField()
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_objective'

class MdlScormSeqRolluprule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    childactivityset = models.CharField(max_length=15)
    minimumcount = models.BigIntegerField()
    minimumpercent = models.FloatField()
    conditioncombination = models.CharField(max_length=3)
    action = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rolluprule'

class MdlScormSeqRolluprulecond(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    rollupruleid = models.BigIntegerField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rolluprulecond'

class MdlScormSeqRulecond(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    ruleconditionsid = models.BigIntegerField()
    refrencedobjective = models.CharField(max_length=255)
    measurethreshold = models.FloatField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_rulecond'

class MdlScormSeqRuleconds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scoid = models.BigIntegerField()
    conditioncombination = models.CharField(max_length=3)
    ruletype = models.IntegerField()
    action = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'mdl_scorm_seq_ruleconds'

class MdlSessions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    state = models.BigIntegerField()
    sid = models.CharField(unique=True, max_length=128)
    userid = models.BigIntegerField()
    sessdata = models.TextField(blank=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstip = models.CharField(max_length=45, blank=True)
    lastip = models.CharField(max_length=45, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_sessions'

class MdlStatsDaily(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_stats_daily'

class MdlStatsMonthly(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_stats_monthly'

class MdlStatsUserDaily(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_stats_user_daily'

class MdlStatsUserMonthly(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_stats_user_monthly'

class MdlStatsUserWeekly(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'mdl_stats_user_weekly'

class MdlStatsWeekly(models.Model):
    id = models.BigIntegerField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_stats_weekly'

class MdlSurvey(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    template = models.BigIntegerField()
    days = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.IntegerField()
    questions = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_survey'

class MdlSurveyAnalysis(models.Model):
    id = models.BigIntegerField(primary_key=True)
    survey = models.BigIntegerField()
    userid = models.BigIntegerField()
    notes = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_survey_analysis'

class MdlSurveyAnswers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    survey = models.BigIntegerField()
    question = models.BigIntegerField()
    time = models.BigIntegerField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_survey_answers'

class MdlSurveyQuestions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.CharField(max_length=255)
    shorttext = models.CharField(max_length=30)
    multi = models.CharField(max_length=100)
    intro = models.CharField(max_length=50)
    type = models.IntegerField()
    options = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_survey_questions'

class MdlTag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(unique=True, max_length=255)
    rawname = models.CharField(max_length=255)
    tagtype = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    flag = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_tag'

class MdlTagCorrelation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tagid = models.BigIntegerField()
    correlatedtags = models.TextField()
    class Meta:
        managed = False
        db_table = 'mdl_tag_correlation'

class MdlTagInstance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tagid = models.BigIntegerField()
    itemtype = models.CharField(max_length=255)
    itemid = models.BigIntegerField()
    tiuserid = models.BigIntegerField()
    ordering = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_tag_instance'

class MdlTempEnroledTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_temp_enroled_template'

class MdlTempLogTemplate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    action = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'mdl_temp_log_template'

class MdlTimezone(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    year = models.BigIntegerField()
    tzrule = models.CharField(max_length=20)
    gmtoff = models.BigIntegerField()
    dstoff = models.BigIntegerField()
    dst_month = models.IntegerField()
    dst_startday = models.IntegerField()
    dst_weekday = models.IntegerField()
    dst_skipweeks = models.IntegerField()
    dst_time = models.CharField(max_length=6)
    std_month = models.IntegerField()
    std_startday = models.IntegerField()
    std_weekday = models.IntegerField()
    std_skipweeks = models.IntegerField()
    std_time = models.CharField(max_length=6)
    class Meta:
        managed = False
        db_table = 'mdl_timezone'

class MdlToolCustomlang(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lang = models.CharField(max_length=20)
    componentid = models.BigIntegerField()
    stringid = models.CharField(max_length=255)
    original = models.TextField()
    master = models.TextField(blank=True)
    local = models.TextField(blank=True)
    timemodified = models.BigIntegerField()
    timecustomized = models.BigIntegerField(blank=True, null=True)
    outdated = models.IntegerField(blank=True, null=True)
    modified = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_tool_customlang'

class MdlToolCustomlangComponents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_tool_customlang_components'

class MdlUpgradeLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    targetversion = models.CharField(max_length=100, blank=True)
    info = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    backtrace = models.TextField(blank=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_upgrade_log'

class MdlUrl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    externalurl = models.TextField()
    display = models.IntegerField()
    displayoptions = models.TextField(blank=True)
    parameters = models.TextField(blank=True)
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_url'

class MdlUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.IntegerField()
    policyagreed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.IntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=40)
    department = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.BigIntegerField()
    lastaccess = models.BigIntegerField()
    lastlogin = models.BigIntegerField()
    currentlogin = models.BigIntegerField()
    lastip = models.CharField(max_length=45)
    secret = models.CharField(max_length=15)
    picture = models.BigIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    mailformat = models.IntegerField()
    maildigest = models.IntegerField()
    maildisplay = models.IntegerField()
    htmleditor = models.IntegerField()
    autosubscribe = models.IntegerField()
    trackforums = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    trustbitmask = models.BigIntegerField()
    imagealt = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_user'

class MdlUserEnrolments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    status = models.BigIntegerField()
    enrolid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_user_enrolments'

class MdlUserInfoCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_user_info_category'

class MdlUserInfoData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    fieldid = models.BigIntegerField()
    data = models.TextField()
    dataformat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_user_info_data'

class MdlUserInfoField(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shortname = models.CharField(max_length=255)
    name = models.TextField()
    datatype = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField()
    categoryid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    required = models.IntegerField()
    locked = models.IntegerField()
    visible = models.IntegerField()
    forceunique = models.IntegerField()
    signup = models.IntegerField()
    defaultdata = models.TextField(blank=True)
    defaultdataformat = models.IntegerField()
    param1 = models.TextField(blank=True)
    param2 = models.TextField(blank=True)
    param3 = models.TextField(blank=True)
    param4 = models.TextField(blank=True)
    param5 = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_user_info_field'

class MdlUserLastaccess(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timeaccess = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_user_lastaccess'

class MdlUserPreferences(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1333)
    class Meta:
        managed = False
        db_table = 'mdl_user_preferences'

class MdlUserPrivateKey(models.Model):
    id = models.BigIntegerField(primary_key=True)
    script = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    iprestriction = models.CharField(max_length=255, blank=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_user_private_key'

class MdlWebdavLocks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    path = models.CharField(max_length=255)
    expiry = models.BigIntegerField()
    userid = models.BigIntegerField()
    recursive = models.IntegerField()
    exclusivelock = models.IntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    owner = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_webdav_locks'

class MdlWiki(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstpagetitle = models.CharField(max_length=255)
    wikimode = models.CharField(max_length=20)
    defaultformat = models.CharField(max_length=20)
    forceformat = models.IntegerField()
    editbegin = models.BigIntegerField()
    editend = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_wiki'

class MdlWikiLinks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subwikiid = models.BigIntegerField()
    frompageid = models.BigIntegerField()
    topageid = models.BigIntegerField()
    tomissingpage = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_wiki_links'

class MdlWikiLocks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pageid = models.BigIntegerField()
    sectionname = models.CharField(max_length=255, blank=True)
    userid = models.BigIntegerField()
    lockedat = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_wiki_locks'

class MdlWikiPages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subwikiid = models.BigIntegerField()
    title = models.CharField(max_length=255)
    cachedcontent = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timerendered = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    readonly = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_wiki_pages'

class MdlWikiSubwikis(models.Model):
    id = models.BigIntegerField(primary_key=True)
    wikiid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_wiki_subwikis'

class MdlWikiSynonyms(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subwikiid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    pagesynonym = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'mdl_wiki_synonyms'

class MdlWikiVersions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pageid = models.BigIntegerField()
    content = models.TextField()
    contentformat = models.CharField(max_length=20)
    version = models.IntegerField()
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_wiki_versions'

class MdlWorkshop(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True)
    introformat = models.IntegerField()
    instructauthors = models.TextField(blank=True)
    instructauthorsformat = models.IntegerField()
    instructreviewers = models.TextField(blank=True)
    instructreviewersformat = models.IntegerField()
    timemodified = models.BigIntegerField()
    phase = models.IntegerField(blank=True, null=True)
    useexamples = models.IntegerField(blank=True, null=True)
    usepeerassessment = models.IntegerField(blank=True, null=True)
    useselfassessment = models.IntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    strategy = models.CharField(max_length=30)
    evaluation = models.CharField(max_length=30)
    gradedecimals = models.IntegerField(blank=True, null=True)
    nattachments = models.IntegerField(blank=True, null=True)
    latesubmissions = models.IntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField(blank=True, null=True)
    examplesmode = models.IntegerField(blank=True, null=True)
    submissionstart = models.BigIntegerField(blank=True, null=True)
    submissionend = models.BigIntegerField(blank=True, null=True)
    assessmentstart = models.BigIntegerField(blank=True, null=True)
    assessmentend = models.BigIntegerField(blank=True, null=True)
    phaseswitchassessment = models.IntegerField()
    conclusion = models.TextField(blank=True)
    conclusionformat = models.IntegerField()
    overallfeedbackmode = models.IntegerField(blank=True, null=True)
    overallfeedbackfiles = models.IntegerField(blank=True, null=True)
    overallfeedbackmaxbytes = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop'

class MdlWorkshopAggregations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_aggregations'

class MdlWorkshopAssessments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    submissionid = models.BigIntegerField()
    reviewerid = models.BigIntegerField()
    weight = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True)
    feedbackauthorformat = models.IntegerField(blank=True, null=True)
    feedbackauthorattachment = models.IntegerField(blank=True, null=True)
    feedbackreviewer = models.TextField(blank=True)
    feedbackreviewerformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_assessments'

class MdlWorkshopAssessmentsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    submissionid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timegraded = models.BigIntegerField()
    timeagreed = models.BigIntegerField()
    grade = models.FloatField()
    gradinggrade = models.IntegerField()
    teachergraded = models.IntegerField()
    mailed = models.IntegerField()
    resubmission = models.IntegerField()
    donotuse = models.IntegerField()
    generalcomment = models.TextField(blank=True)
    teachercomment = models.TextField(blank=True)
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_assessments_old'

class MdlWorkshopCommentsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    mailed = models.IntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_comments_old'

class MdlWorkshopElementsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.IntegerField()
    description = models.TextField()
    scale = models.IntegerField()
    maxscore = models.IntegerField()
    weight = models.IntegerField()
    stddev = models.FloatField()
    totalassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_elements_old'

class MdlWorkshopGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    assessmentid = models.BigIntegerField()
    strategy = models.CharField(max_length=30)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    peercomment = models.TextField(blank=True)
    peercommentformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_grades'

class MdlWorkshopGradesOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    feedback = models.TextField()
    grade = models.IntegerField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_grades_old'

class MdlWorkshopOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    wtype = models.IntegerField()
    nelements = models.IntegerField()
    nattachments = models.IntegerField()
    phase = models.IntegerField()
    format = models.IntegerField()
    gradingstrategy = models.IntegerField()
    resubmit = models.IntegerField()
    agreeassessments = models.IntegerField()
    hidegrades = models.IntegerField()
    anonymous = models.IntegerField()
    includeself = models.IntegerField()
    maxbytes = models.BigIntegerField()
    submissionstart = models.BigIntegerField()
    assessmentstart = models.BigIntegerField()
    submissionend = models.BigIntegerField()
    assessmentend = models.BigIntegerField()
    releasegrades = models.BigIntegerField()
    grade = models.IntegerField()
    gradinggrade = models.IntegerField()
    ntassessments = models.IntegerField()
    assessmentcomps = models.IntegerField()
    nsassessments = models.IntegerField()
    overallocation = models.IntegerField()
    timemodified = models.BigIntegerField()
    teacherweight = models.IntegerField()
    showleaguetable = models.IntegerField()
    usepassword = models.IntegerField()
    password = models.CharField(max_length=32)
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_old'

class MdlWorkshopRubricsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    rubricno = models.IntegerField()
    description = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_rubrics_old'

class MdlWorkshopStockcommentsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_stockcomments_old'

class MdlWorkshopSubmissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    example = models.IntegerField(blank=True, null=True)
    authorid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    contentformat = models.IntegerField()
    contenttrust = models.IntegerField()
    attachment = models.IntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True)
    feedbackauthorformat = models.IntegerField(blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    late = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'mdl_workshop_submissions'

class MdlWorkshopSubmissionsOld(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    mailed = models.IntegerField()
    description = models.TextField()
    gradinggrade = models.IntegerField()
    finalgrade = models.IntegerField()
    late = models.IntegerField()
    nassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True)
    newid = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshop_submissions_old'

class MdlWorkshopallocationScheduled(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    enabled = models.IntegerField()
    submissionend = models.BigIntegerField()
    timeallocated = models.BigIntegerField(blank=True, null=True)
    settings = models.TextField(blank=True)
    resultstatus = models.BigIntegerField(blank=True, null=True)
    resultmessage = models.CharField(max_length=1333, blank=True)
    resultlog = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopallocation_scheduled'

class MdlWorkshopevalBestSettings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    comparison = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopeval_best_settings'

class MdlWorkshopformAccumulative(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    grade = models.BigIntegerField()
    weight = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_accumulative'

class MdlWorkshopformComments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_comments'

class MdlWorkshopformNumerrors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    descriptiontrust = models.BigIntegerField(blank=True, null=True)
    grade0 = models.CharField(max_length=50, blank=True)
    grade1 = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_numerrors'

class MdlWorkshopformNumerrorsMap(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    nonegative = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_numerrors_map'

class MdlWorkshopformRubric(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric'

class MdlWorkshopformRubricConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    layout = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric_config'

class MdlWorkshopformRubricLevels(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True)
    definitionformat = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mdl_workshopform_rubric_levels'


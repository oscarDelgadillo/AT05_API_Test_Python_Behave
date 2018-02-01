def before_all(context):
    print("-------------- BEFORE ALL --------------")


def before_feature(context, feature):
    if 'try' in feature.tags:
        print("*************** FEATURE TRY TAGS ***************")
    if 'Test' in feature.name:
        print("++++++++++++++++ FEATURE TEST NAME ++++++++++++++++")


def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print("////////////// SCENARIO TAGS //////////////")
    if 'Test' in scenario.name:
        print("=============== SCENARIO TEST ===============")


def before_step(context, step):
    print("STEP", step.name)
    print("STEP KEYWORD", step.keyword)
    print("STEP STATUS", step.status)

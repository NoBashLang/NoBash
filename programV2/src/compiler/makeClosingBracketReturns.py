




def makeCBRF(lines, bracesInfo):
    closingBracketReturnFunctions = {"for":"__jumpBackFor__(}", "if": "__cbrfIf__(}",\
        "else":"__cbrfElse__(}", "func": "__funcReturn__()", "elif": "__cbrfElif__(}", "while": "__jumpBackWhile__(}"}
    for id, info in bracesInfo.items():
        endOp, ctrlFlowStatement = info["endOp"], info["ctrlFlowStatement"]
        if str(endOp) in lines.keys():
            lines[str(endOp)][0] = lines[str(endOp)][0].replace("}"+str(id), "")
            if not lines[str(endOp)][0].strip():
                del lines[str(endOp)][0]
            if ctrlFlowStatement != "func":
                lines[str(endOp)]\
                    .insert(-1, closingBracketReturnFunctions[ctrlFlowStatement]+str(id)+")")
            else: 
                lines[str(endOp)].insert(-1, closingBracketReturnFunctions[ctrlFlowStatement])
            
    return lines
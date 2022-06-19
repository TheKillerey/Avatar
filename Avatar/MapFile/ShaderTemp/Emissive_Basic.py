"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { EM_Red, EM_Green, EM_Blue, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 3.85, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 0.6, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Emissive_Basic"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
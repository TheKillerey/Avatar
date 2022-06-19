"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Textures"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Mask_Name"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Bias"
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0, 0.02, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Step_Amount"
                value: vec4 = { 0.7, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Sin_Values"
                value: vec4 = { 10, 1, -1.5, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BaseColor"
                value: vec4 = { 0.007843138, 1, 0.07058824, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "AnimatedUV_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "StaticUV_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 10, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_ALPHA_STEP"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/SinFade_Alpha"
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
"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "FlipBook_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Flipbook_Name"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Noise_Amp"
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "FlipBook_Dims"
                value: vec4 = { 4, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "FlipBook_FPS"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 1.2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flicker_Speed"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/FlickerAlpha_FlipBook"
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
"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Texture_Name"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Emissive_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Emissive_Name"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Selector"
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Dims"
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Selector"
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Dims"
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Speed"
                value: vec4 = { 5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_MinMax"
                value: vec4 = { 0.939999998, 1.10000002, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Offset"
                value: vec4 = { 1, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_RED_CHANNEL_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GREEN_CHANNEL_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_BLUE_CHANNEL_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_FLICKER"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_GlowSign"
                        cullEnable: bool = false
                    }
                }
            }
        }
    }
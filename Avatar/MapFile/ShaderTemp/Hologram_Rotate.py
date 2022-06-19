"Material_Name" = StaticMaterialDef {
        name: string = "Material_Name"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Mask_Name"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Noise"
                textureName: string = "ASSETS/Shared/Materials/Default/Noise.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/SRX/Map_Name/Texture_Name"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Distortion_TimeSpeed"
                value: vec4 = { 0.035, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Scale"
                value: vec4 = { 0.5, 2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Distortion_Amount"
                value: vec4 = { 0.005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Distortion_ScrollSpeed"
                value: vec4 = { -0.01, -0.03, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScanLine_ScrollSpeed"
                value: vec4 = { -0.05, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Emissive_Intensity"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScanLines1"
                value: vec4 = { 1, -2, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Color"
                value: vec4 = { 0, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Base_Color"
                value: vec4 = { 0.05882353, 0.9529412, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Final_Alpha"
                value: vec4 = { 0.68, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { -1, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/Hologram_Rotate"
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
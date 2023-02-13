$Env:CONDA_EXE = "/Users/66j/Documents/ORNL/code/g2full/bin/conda"
$Env:_CE_M = ""
$Env:_CE_CONDA = ""
$Env:_CONDA_ROOT = "/Users/66j/Documents/ORNL/code/g2full"
$Env:_CONDA_EXE = "/Users/66j/Documents/ORNL/code/g2full/bin/conda"
$CondaModuleArgs = @{ChangePs1 = $True}
Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs
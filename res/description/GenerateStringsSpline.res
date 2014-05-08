CONTAINER GenerateStringsSpline {
	
	NAME GenerateStringsSpline;

	GROUP GenerateStringsSplineSettings
	{
		LONG Count {MINEX; MIN 1; MAX 500;}
		LONG RandomSeed {MINEX; MIN 0; }
		VECTOR Scale {MIN 0.0; STEP 0.01; UNIT METER; }
	}
}
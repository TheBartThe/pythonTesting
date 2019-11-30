pipeline{


	agent any

	stages{

		stage("-----Update git repo-----") {

			steps{

				sh '''ssh vieran96@python-tests << EOF
				cd pythonTesting

				git pull'''
			}
		}

		stage("-----Create init files-----") {

			steps{

				sh '''ssh vieran96@python-tests << EOF
				touch ./pythonTesting/tests/__init__.py
				touch ./pythonTesting/pythonExercises/__init__.py'''

			}
		}
		stage("-----Create test-----") {

			steps{
				sh '''ssh vieran96@python-tests << EOF
				pytest pythonTesting/tests/count_test.py'''
			}

		}

	}

}
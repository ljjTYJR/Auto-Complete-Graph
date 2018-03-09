#ifndef AUTOCOMPLETEGRAPH_VERTEXSE2ROBOTPOSE_10112017
#define AUTOCOMPLETEGRAPH_VERTEXSE2ROBOTPOSE_10112017

#include "g2o/types/slam2d/vertex_se2.h"
#include "EdgeInterfaceMalcolm.hpp"
#include "opencv2/core/core.hpp"

namespace AASS {
namespace acg{	
	
class VertexSE2RobotPose : public g2o::VertexSE2
  {
	public:
		EIGEN_MAKE_ALIGNED_OPERATOR_NEW
		VertexSE2RobotPose() :  _index_graphmap(-1), g2o::VertexSE2(){}
		
	protected:
		std::shared_ptr<perception_oru::NDTMap> _map;
		Eigen::Affine3d _T;
		double _time;
		int _index_graphmap;
	public:
		g2o::SE2 initial_transfo;
		cv::Mat img;
		
		std::shared_ptr<perception_oru::NDTMap>& getMap(){return _map;}
		const std::shared_ptr<perception_oru::NDTMap>& getMap() const {return _map;}
		void setMap(const std::shared_ptr<perception_oru::NDTMap>& map){_map = map;}
		Eigen::Affine3d getPose(){return _T;}
		const Eigen::Affine3d& getPose() const {return _T;}
		void setPose(const Eigen::Affine3d& T) {_T = T;}
		void setTime(double t){_time = t;}
		double getTime(){return _time;}

		void setIndexGraphMap(int i){_index_graphmap = i;}
		int getIndexGraphMap(int i){return _index_graphmap;}


  };

}
}
#endif